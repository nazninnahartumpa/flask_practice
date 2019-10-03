from flask import Flask, render_template, make_response, Markup,request, jsonify
from forms import SignupForm

app = Flask(__name__, static_folder="static", template_folder="templates")
app.config['SECRET_KEY'] = 'sdkqwe9873498kqjwdskajshdiqv6e55552@fdfgrwe92qew09qe'


@app.route("/", methods=['GET'])
def index():
    return render_template("index.html")


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    """Signup Form."""
    signup_form = SignupForm()
    if request.method == 'POST':
        if signup_form.validate():
            flash('Logged in successfully.')
            # return render_template('dashboard.html', template="dashbord-template")
    return render_template('/signup.html', form=signup_form, template="form-page")


if __name__ == "__main__":
    app.run( debug="True", host="0.0.0.0", port="5000")
