from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)

# Configure the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///portfolio.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app import db

class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    link = db.Column(db.String(200), nullable=False)
    created_at = db.Column(db.DateTime, server_default=db.func.now(), nullable=False)

class BlogPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, server_default=db.func.now(), nullable=False)

class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    message = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, server_default=db.func.now(), nullable=False)


    from models import Project, BlogPost, Contact

# Projects Endpoints
@app.route('/projects', methods=['POST'])
def add_project():
    data = request.get_json()
    new_project = Project(title=data['title'], description=data['description'], link=data['link'])
    db.session.add(new_project)
    db.session.commit()
    return jsonify({"message": "Project added successfully"}), 201

@app.route('/projects', methods=['GET'])
def get_all_projects():
    projects = Project.query.all()
    return jsonify([{"id": p.id, "title": p.title, "description": p.description, "link": p.link} for p in projects])

@app.route('/projects/<int:project_id>', methods=['GET'])
def get_single_project(project_id):
    project = Project.query.get_or_404(project_id)
    return jsonify({"id": project.id, "title": project.title, "description": project.description, "link": project.link})

@app.route('/projects/<int:project_id>', methods=['PUT'])
def edit_project(project_id):
    project = Project.query.get_or_404(project_id)
    data = request.get_json()
    project.title = data['title']
    project.description = data['description']
    project.link = data['link']
    db.session.commit()
    return jsonify({"message": "Project updated successfully"})

@app.route('/projects/<int:project_id>', methods=['DELETE'])
def delete_project(project_id):
    project = Project.query.get_or_404(project_id)
    db.session.delete(project)
    db.session.commit()
    return jsonify({"message": "Project deleted successfully"})

# Blog Posts Endpoints
@app.route('/blog-posts', methods=['POST'])
def add_blog_post():
    data = request.get_json()
    new_blog_post = BlogPost(title=data['title'], content=data['content'])
    db.session.add(new_blog_post)
    db.session.commit()
    return jsonify({"message": "Blog post added successfully"}), 201

@app.route('/blog-posts', methods=['GET'])
def get_all_blog_posts():
    blog_posts = BlogPost.query.all()
    return jsonify([{"id": p.id, "title": p.title, "content": p.content} for p in blog_posts])

@app.route('/blog-posts/<int:post_id>', methods=['GET'])
def get_single_blog_post(post_id):
    blog_post = BlogPost.query.get_or_404(post_id)
    return jsonify({"id": blog_post.id, "title": blog_post.title, "content": blog_post.content})

@app.route('/blog-posts/<int:post_id>', methods=['PUT'])
def edit_blog_post(post_id):
    blog_post = BlogPost.query.get_or_404(post_id)
    data = request.get_json()
    blog_post.title = data['title']
    blog_post.content = data['content']
    db.session.commit()
    return jsonify({"message": "Blog post updated successfully"})

@app.route('/blog-posts/<int:post_id>', methods=['DELETE'])
def delete_blog_post(post_id):
    blog_post = BlogPost.query.get_or_404(post_id)
    db.session.delete(blog_post)
    db.session.commit()
    return jsonify({"message": "Blog post deleted successfully"})

# Contact Information Endpoints
@app.route('/contacts', methods=['POST'])
def add_contact():
    data = request.get_json()
    new_contact = Contact(name=data['name'], email=data['email'], message=data['message'])
    db.session.add(new_contact)
    db.session.commit()
    return jsonify({"message": "Contact added successfully"}), 201

@app.route('/contacts/<int:contact_id>', methods=['PUT'])
def edit_contact(contact_id):
    contact = Contact.query.get_or_404(contact_id)
    data = request.get_json()
    contact.name = data['name']
    contact.email = data['email']
    contact.message = data['message']
    db.session.commit()
    return jsonify({"message": "Contact information updated successfully"})

@app.route('/contacts/<int:contact_id>', methods=['DELETE'])
def delete_contact(contact_id):
    contact = Contact.query.get_or_404(contact_id)
    db.session.delete(contact)
    db.session.commit()
    return jsonify({"message": "Contact information deleted successfully"})

if __name__ == "__main__":
    app.run(debug=True)
