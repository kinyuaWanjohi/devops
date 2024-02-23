from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Set default username and password
DEFAULT_USERNAME = 'admin'
DEFAULT_PASSWORD = 'admin'

# Dummy data for the second page
SECOND_PAGE_FIELDS = ['First Name', 'Last Name', 'ID Number', 'Telephone Number', 'Passport Photo']


@app.route('/')
def login():
    return render_template('login.html')


@app.route('/verify', methods=['POST'])
def verify():
    username = request.form.get('username')
    password = request.form.get('password')

    if username == DEFAULT_USERNAME and password == DEFAULT_PASSWORD:
        return render_template('second_page.html', fields=SECOND_PAGE_FIELDS)
    else:
        return "Incorrect username or password. Please try again."


if __name__ == '__main__':
    app.run(debug=True)
