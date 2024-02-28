from flask import Flask, request, send_file
import sys

from application_confirm import check_info


application = Flask(__name__)


@application.route("/")
def main_page():
    template = ""
    with open("./src/main.html", "r") as t:
        template = t.read()
    return template


@application.route("/application_confirm/")
def entry():
    template = ""
    with open("./application_confirm/form.html", "r") as t:
        template = t.read()
    return template


@application.route("/application_confirm/browse_info", methods=['POST'])
def browse():
    phone_num = request.form['phone_num']
    template = check_info.check(phone_num)
    return template


if __name__ == "__main__":
    application.run(host='0.0.0.0', port=int(sys.argv[1]))
