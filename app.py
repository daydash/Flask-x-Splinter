from selenium import webdriver
from splinter import Browser
import time
from flask import Flask,request, jsonify

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/loginToWW", methods=["POST"])
def login():
    username = request.json['username']
    password = request.json['password']

    print(username, password)

    browser = Browser('chrome')
    browser.visit('https://vaishu-15.github.io/WealthWise/')

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

if __name__ == "__main__":
    app.run(debug=True)