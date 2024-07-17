"""
Launch the Webtile Flask Application
"""
import os
from flask import Flask, request, render_template, redirect, url_for
from scripts.utils import Environment, get_post_content,get_all_posts, initialize_logger, parse_arguments

# Gunicorn does not pass any custom command-line arguments to the application
if 'gunicorn' in os.getenv('SERVER_SOFTWARE', ''):
    # Default to production environment
    env = Environment('production')
    verbose = False
else:
    # Load command line arguments
    args = parse_arguments()
    env = Environment(args.environment)
    verbose = args.verbose

# Load app configs
app = Flask(__name__)
app.logger = initialize_logger(
    "webtile",
    log_directory=env.log_directory,
    log_name=env.log_name,
    log_format=env.log_format,
    verbose=verbose
)

@app.after_request
def log_response_info(response):
    """
    Define logging for requests to server
    """

    # Log Get Request
    app.logger.info(f'{request.remote_addr} - - "{request.method} {request.full_path} {request.scheme}" {response.status_code} -')

    # Add headers in debug mode
    if verbose:
        header_log_message = '{'
        for key, value in request.headers.items():
            header_log_message += f'"{key}";"{value}",'
        header_log_message = header_log_message[:-1] + '}'
        app.logger.debug(header_log_message)

    return response

@app.route('/')
def home():
    """
    Server landing page
    """
    return render_template('home.html')

@app.route('/blog')
def blog():
    """
    List featured, latest, and archived posts
    """

    # Get all posts
    all_posts = get_all_posts("posts")

    # Load latest posts
    for post in all_posts:
        post = get_post_content("posts", post, 200)

    # Get featured post
    try:
        featured_post = get_post_content("posts", {'filename': env.featured_post}, 600)

    # Fall back to latest post if error
    except FileNotFoundError:
        featured_post = all_posts[0]

    return render_template(
        'blog.html',
        featured_post=featured_post,
        latest_post=all_posts[:3],
        all_posts=all_posts
    )

@app.route('/community')
def community():
    """
    Showcase static content
    """

    # Get all posts
    all_posts = get_all_posts("community")

    # Load latest posts
    for post in all_posts:
        post = get_post_content("community", post)

    return render_template('community.html', all_posts=all_posts)

@app.route('/post/<filename>')
def post(filename):
    """
    Return requested articles
    """
    # Input Validation
    posts_directory = os.path.abspath("posts")
    requested_file = os.path.abspath(os.path.join(posts_directory, filename))
    if not os.path.isfile(requested_file):
        return redirect(url_for('blog'))

    post = get_post_content('posts', {'filename': filename})

    return render_template('article.html', post=post)

if __name__ == '__main__':
    app.run(debug=verbose)
