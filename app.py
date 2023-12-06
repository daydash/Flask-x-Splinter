from selenium import webdriver
from splinter import Browser
import time
from flask import Flask,request, jsonify
from waitress import serve
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app)

@app.route("/")
# @cross_origin()
def hello_world():
    return "<p>Hello, World!!</p>"

@app.route("/loginToWW", methods=["POST"])
# @cross_origin()
def login():
    username = request.json['username']
    password = request.json['password']

    print(username, password)

    try:
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')  # Run Chrome in headless mode
        driver = webdriver.Chrome(options=options)

        browser = Browser("chrome")
        browser.visit('https://vaishu-15.github.io/WealthWise/')
    except Exception as error:
        print("Error in Browser instance ->\n", error)

    getStarted = browser.links.find_by_partial_href('login.html')
    getStarted.click()

    time.sleep(1)
    emailField = browser.find_by_name("logemail")
    emailField.fill(username)
    passwordField = browser.find_by_name("logpass")
    passwordField.fill(password)

    time.sleep(1)
    submit = browser.find_by_id('submitButton')
    submit.click()

    time.sleep(1)
    submitAgain = browser.find_by_id('submitButton')
    submitAgain.click()

    time.sleep(1)
    browser.execute_script("document.getElementById('submitButton').click()")

    return username

mode = "prod"

if __name__ == "__main__":
    if mode == "prod":
        print("in prod")
        serve(app, host='0.0.0.0', port=5000, threads=1)
    else:
        print("in dev")
        app.run(debug=True)