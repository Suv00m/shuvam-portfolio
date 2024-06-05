from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import yaml
import logging

logger = logging.getLogger(__name__)
app = Flask(__name__)
app.jinja_env.filters['zip'] = zip

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/blog")
def blog():
    # list_example = ['Alvin', 'Simon', 'Theodore','shuvam']
    with open('blog.yaml') as file:
         data = yaml.safe_load(file)
         print("data",data)
         blog_data = data['blog']
         print("blog_data",blog_data)
         posts_data = blog_data['posts']
         print("posts_data",posts_data)
         print(file)
    return render_template("blog.html",posts=posts_data)

@app.route("/talk")
def post():
    return render_template("talk.html")

# if __name__ == "__main__":
#     app.run(debug=True)
