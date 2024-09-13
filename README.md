# Personal Portfolio API

This API allows you to manage projects, blog posts, and contact information for a personal portfolio website.

## Endpoints

### Projects
- `POST /projects`: Add a new project
- `GET /projects`: Get all projects
- `GET /projects/<int:project_id>`: Get a single project by ID
- `PUT /projects/<int:project_id>`: Edit a project by ID
- `DELETE /projects/<int:project_id>`: Delete a project by ID

### Blog Posts
- `POST /blog-posts`: Add a new blog post
- `GET /blog-posts`: Get all blog posts
- `GET /blog-posts/<int:post_id>`: Get a single blog post by ID
- `PUT /blog-posts/<int:post_id>`: Edit a blog post by ID
- `DELETE /blog-posts/<int:post_id>`: Delete a blog post by ID

### Contact Information
- `POST /contacts`: Add new contact information
- `PUT /contacts/<int:contact_id>`: Edit contact information by ID
- `DELETE /contacts/<int:contact_id>`: Delete contact information by ID
