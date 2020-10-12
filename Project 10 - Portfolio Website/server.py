"""
This module implements the Portfolio Website exercise of the Section 19 of the course.
"""

import csv
import flask

# Create the flask object
app = flask.Flask(__name__)


@app.route('/')
def home():
    return flask.render_template('index.html')


@app.route('/<string:page_name>')
def html_page(page_name):
    return flask.render_template(page_name)


def write_to_csv(data):
    with open('database.csv', newline='', mode='a') as database:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]

        csv_writer = csv.writer(database, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, message])


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if flask.request.method == 'POST':
        try:
            data = flask.request.form.to_dict()
            write_to_csv(data)
            return flask.redirect('/thankyou.html')
        except IOError:
            return 'Error saving to the database'
    else:
        return 'Something went wrong. Try again!'
