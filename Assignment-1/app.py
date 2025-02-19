from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    slides = [
        {"text": "Welcome to Flask Bootstrap", "color": "#FF5733"},
        {"text": "Responsive and Attractive Design", "color": "#33A1FF"},
        {"text": "Easy to Use and Modern", "color": "#33FF57"},
    ]
    cards = [
        {"title": "Flask Framework", "text": "A lightweight and flexible Python web framework."},
        {"title": "Bootstrap Design", "text": "Create responsive and modern UI with Bootstrap."},
        {"title": "Web Development", "text": "Learn full-stack development with Flask."},
    ]
    return render_template('index.html', title="Home", subtitle="Welcome to our Flask Web App!", slides=slides, cards=cards)

@app.route('/about')
def about():
    return render_template('about.html', title="About Us", subtitle="Learn more about our mission and team.")

@app.route('/services')
def services():
    services_list = [
        {"name": "Web Development", "description": "Custom web applications using Flask."},
        {"name": "UI/UX Design", "description": "Beautiful and user-friendly designs."},
        {"name": "API Development", "description": "Robust and scalable API solutions."},
    ]
    return render_template('services.html', title="Our Services", subtitle="What we offer", services=services_list)

@app.route('/contact')
def contact():
    return render_template('contact.html', title="Contact Us", subtitle="Get in touch with us!")

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)
