import datetime
from flask import Flask, render_template, url_for, flash, redirect
from forms import LoginForm, RegistrationForm

app = Flask(__name__)
app.url_map.strict_slashes = False
app.config['SECRET_KEY'] = 'd24cea3cd7757ef7e80ca62e1c1a385e'

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


if __name__ == "__main__":
    app.run(debug=True)
    