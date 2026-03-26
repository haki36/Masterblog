import json
import os
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    file_path = os.path.join(app.root_path, 'data', 'posts.json')
    with open(file_path, "r", encoding="utf-8") as f:
        blog_posts = json.load(f)
    return render_template('index.html', posts=blog_posts)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)