from flask import Blueprint, render_template, redirect, url_for, flash
from pharmakart.forms import LoginForm, RegistrationForm


bp = Blueprint('route', __name__, url_prefix='/')

@bp.route("/")
@bp.route("/home")
def home():
    return render_template("route.home.html")


@bp.route("/about/")
def about():
    return render_template("about.html/")


@bp.route("/featured-services/")
def services():
    return render_template("services.html")


@bp.route("/contact/")
def contact():
    return render_template("contact.html")

@bp.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template("register.html", title='Register', form=form)

@bp.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template("login.html", title='Login', form=form)


