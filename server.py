from flask import Flask, render_template, url_for, request
import csv

app = Flask(__name__)


@app.route("/")
def home():
    return render_template('index.html')


@app.route("/<string:page_name>")
def html_page(page_name):
    return render_template(page_name)


def write_to_file(data):
    with open('database.txt', mode='a') as database:
        email = data['email']
        message = data['message']
        name = data['name']

        file = database.write(
            f'\n Name: {name}, Email: {email} \n Message: {message}')


def write_to_file(data):
    with open('database2.csv', newline='', mode='a') as database2:
        email = data['email']
        message = data['message']
        name = data['name']
        csv_writer = csv.writer(database2, delimiter=',',
                                quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([name, email, message])


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict()
        write_to_file(data)
        return 'Form Submitted'
    else:
        return 'something went wrong, try again.'
