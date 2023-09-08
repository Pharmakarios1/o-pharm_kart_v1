import os
from flask import Flask, render_template, redirect, flash, url_for
from pharmakart.tools import generate_uri_from_file
from pharmakart.forms import LoginForm, RegistrationForm



def create_app(test_config=None):
    app = Flask(__name__)
    app.url_map.strict_slashes = False
    app.config['SECRET_KEY'] = 'd24cea3cd7757ef7e80ca62e1c1a385e'

    database_URI = generate_uri_from_file('db_config.yml')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_DATABASE_URI'] = database_URI

    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)

    else:
        app.config.from_mapping(test_config)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    @app.route("/")
    @app.route("/home")
    def home():
        return render_template("home.html")


    @app.route("/about/")
    def about():
        return render_template("about.html/")


    @app.route("/featured-services/")
    def services():
        return render_template("services.html")


    @app.route("/contact/")
    def contact():
        return render_template("contact.html")
    
    @app.route("/register", methods=['GET', 'POST'])
    def register():
        form = RegistrationForm()
        if form.validate_on_submit():
            flash(f'Account created for {form.username.data}!', 'success')
            return redirect(url_for('home'))
        return render_template("register.html", title='Register', form=form)

    @app.route("/login", methods=['GET', 'POST'])
    def login():
        form = LoginForm()
        if form.validate_on_submit():
            if form.email.data == 'admin@blog.com' and form.password.data == 'password':
                flash('You have been logged in!', 'success')
                return redirect(url_for('home'))
            else:
                flash('Login Unsuccessful. Please check username and password', 'danger')
        return render_template("login.html", title='Login', form=form)

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True, host='0.0.0.0')
