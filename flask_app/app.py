from flask import Flask, render_template

app = Flask(__name__)

# Home Page
@app.route('/')
def home():
    slides = [
        {"text": "Welcome to Flask Bootstrap", "color": "#007bff"},
        {"text": "Build Responsive Websites", "color": "#28a745"},
        {"text": "Deploy with Ease", "color": "#dc3545"}
    ]
    
    cards = [
        {"title": "Fast Development", "text": "Flask makes development easy and quick."},
        {"title": "Bootstrap UI", "text": "Beautiful, responsive designs with Bootstrap."},
        {"title": "Easy Deployment", "text": "Deploy your Flask apps with minimal setup."}
    ]

    return render_template('index.html', title="Welcome to Flask", subtitle="A lightweight and flexible framework", slides=slides, cards=cards)

# About Page
@app.route('/about')
def about():
    return render_template('about.html', title="About Us", subtitle="Learn more about what we do")

# Services Page
@app.route('/services')
def services():
    services_list = [
        {"name": "Web Development", "description": "We create high-quality web applications."},
        {"name": "API Development", "description": "Build powerful and scalable APIs."},
        {"name": "Cloud Deployment", "description": "Deploy your applications on the cloud."}
    ]
    
    return render_template('services.html', title="Our Services", subtitle="What we offer", services=services_list)

# Contact Page
@app.route('/contact')
def contact():
    return render_template('contact.html', title="Contact Us", subtitle="Get in touch with us")

# Error Handling
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html', title="Page Not Found"), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html', title="Internal Server Error"), 500

if __name__ == '__main__':
    app.run(debug=True)
