"""
Simple Flask blog application using a JSON file as storage.

This app supports the basic CRUD operations for blog posts:
- Create new posts
- Read and display all posts
- Update existing posts
- Delete posts

The blog posts are stored in data/posts.json.
"""

import json
import os
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

POSTS_FILE = os.path.join(app.root_path, 'data', 'posts.json')


def load_posts():
    """
    Load all blog posts from the JSON file.
    Returns:
        list: A list of blog post dictionaries.
    Raises:
        FileNotFoundError: If the JSON file does not exist.
        json.JSONDecodeError: If the JSON file contains invalid JSON.
    """
    with open(POSTS_FILE, 'r', encoding='utf-8') as f:
        return json.load(f)


def save_posts(posts):
    """
    Save all blog posts to the JSON file.
    Args:
        posts (list): A list of blog post dictionaries to save.
    Raises:
        OSError: If the file cannot be written.
    """
    with open(POSTS_FILE, 'w', encoding='utf-8') as f:
        json.dump(posts, f, indent=4)


@app.route('/')
def index():
    """
    Display the homepage with all blog posts.
    Returns:
        Response: Rendered index page with all posts,
        or an error message if the JSON file is invalid.
    """
    try:
        blog_posts = load_posts()
    except FileNotFoundError:
        blog_posts = []
    except json.JSONDecodeError:
        return "Error: posts.json is an invalid JSON.", 500

    return render_template('index.html', posts=blog_posts)


@app.route('/add', methods=['GET', 'POST'])
def add():
    """
    Display the add form and handle creation of a new blog post.
    GET:
        Render the form for creating a new post.
    POST:
        Read form data, create a new post, save it to the JSON file,
        and redirect to the homepage.
    Returns:
        Response: Rendered add page, redirect to homepage,
        or an error message if loading/saving fails.
    """
    if request.method == 'POST':
        author = request.form.get('author')
        title = request.form.get('title')
        content = request.form.get('content')

        try:
            blog_posts = load_posts()
        except FileNotFoundError:
            blog_posts = []
        except json.JSONDecodeError:
            return "Error: posts.json is an invalid JSON.", 500

        new_id = max(post['id'] for post in blog_posts) + 1 if blog_posts else 1

        new_post = {
            'id': new_id,
            'author': author,
            'title': title,
            'content': content
        }

        blog_posts.append(new_post)

        try:
            save_posts(blog_posts)
        except OSError:
            return "Error: could not write to posts.json.", 500

        return redirect(url_for('index'))

    return render_template('add.html')


@app.route('/delete/<int:post_id>')
def delete(post_id):
    """
    Delete a blog post by its ID.
    Args:
        post_id (int): The ID of the post to delete.
    Returns:
        Response: Redirect to homepage after deletion,
        or an error message if the file does not exist.
    """
    try:
        blog_posts = load_posts()
        blog_posts = [post for post in blog_posts if post['id'] != post_id]
        save_posts(blog_posts)
        return redirect(url_for('index'))
    except FileNotFoundError:
        return {"error": "JSON file not found"}, 500
    except json.JSONDecodeError:
        return "Error: posts.json is an invalid JSON.", 500
    except OSError:
        return "Error: could not write to posts.json.", 500


@app.route('/update/<int:post_id>', methods=['GET', 'POST'])
def update(post_id):
    """
    Display the update form and handle editing of an existing blog post.
    Args:
        post_id (int): The ID of the post to update.
    GET:
        Render the update form pre-filled with the current post data.
    POST:
        Update the selected post with the submitted form data,
        save the changes, and redirect to the homepage.
    Returns:
        Response: Rendered update page, redirect to homepage,
        404 if post is not found, or an error message if loading/saving fails.
    """
    try:
        blog_posts = load_posts()
    except FileNotFoundError:
        return "Error: posts.json file not found.", 500
    except json.JSONDecodeError:
        return "Error: posts.json is an invalid JSON.", 500

    post = None
    for p in blog_posts:
        if p['id'] == post_id:
            post = p
            break

    if post is None:
        return "Post not found", 404

    if request.method == 'POST':
        post['author'] = request.form.get('author')
        post['title'] = request.form.get('title')
        post['content'] = request.form.get('content')

        try:
            save_posts(blog_posts)
        except OSError:
            return "Error: could not write to posts.json.", 500

        return redirect(url_for('index'))

    return render_template('update.html', post=post)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
