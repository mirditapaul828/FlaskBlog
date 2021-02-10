from flask import Blueprint, render_template, request
from flaskblog.models import Post

main = Blueprint('main', __name__)
    
#Home page
@main.route('/')  #Use route decorator to set dedicated route (Ex. Home page)
@main.route('/home')
def home():
    page = request.args.get('page', 1, type=int)
    posts = Post.query.order_by(Post.date_posted.desc()).paginate(page=page, per_page=5)
    return render_template('home.html', posts=posts)

#About Page
@main.route('/about')
def about():
    return render_template('about.html', title='About')