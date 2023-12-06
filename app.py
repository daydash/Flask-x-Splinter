from selenium import webdriver
from splinter import Browser
# import time
from flask import Flask
# ,request, jsonify
from waitress import serve
from flask_cors import CORS
from selenium.webdriver.chrome.options import Options

app = Flask(__name__)
cors = CORS(app)

@app.route("/")
# @cross_origin()
def hello_world():
    return "<p>Hello, World!!</p>"


@app.route("/search2")
def search2():
    print("search2 hitted\n\n\n\n\n")
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    # chrome_options.add_argument('--disable-gpu')
    driver = webdriver.Chrome(options=chrome_options)
    # driver = webdriver.Chrome()
    driver.get("https://www.google.com")

    search_box = driver.find_element("name","q")
    search_box.send_keys("chatgpt")
    search_box.submit()

    print("search2 end\n\n\n\n\n")
    return "hello"

@app.route("/search")
def search():
    from splinter import Browser

    browser = Browser()

    browser.visit('http://google.com')
    input_element = browser.find_by_name('q')
    input_element.fill('splinter - python acceptance testing for web applications')

    button_element = browser.find_by_name('btnK')[1]
    button_element.click()

    if browser.is_text_present('splinter.readthedocs.io'):
        print("Yes, the official website was found!")
    else:
        print("No, it wasn't found... We need to improve our SEO techniques")

    browser.quit()

# @app.route("/loginToWW", methods=["POST"])
# @cross_origin()
# def login():
#     username = request.json['username']
#     password = request.json['password']

#     print(username, password)

#     try:
#         # options = webdriver.ChromeOptions()
#         # options.add_argument('--headless') 
#         # options.add_argument('--disable-gpu')
#         # driver = webdriver.Chrome(options=options)

#         browser = Browser()
#         browser.visit('https://vaishu-15.github.io/WealthWise/')
#     except Exception as error:
#         print("Error in Browser instance ->\n", error)

#     getStarted = browser.links.find_by_partial_href('login.html')
#     getStarted.click()

#     time.sleep(1)
#     emailField = browser.find_by_name("logemail")
#     emailField.fill(username)
#     passwordField = browser.find_by_name("logpass")
#     passwordField.fill(password)

#     time.sleep(1)
#     submit = browser.find_by_id('submitButton')
#     submit.click()

#     time.sleep(1)
#     submitAgain = browser.find_by_id('submitButton')
#     submitAgain.click()

#     time.sleep(1)
#     browser.execute_script("document.getElementById('submitButton').click()")

#     return username

mode = "prod"

if __name__ == "__main__":
    if mode == "prod":
        print("in prod")
        serve(app, host='0.0.0.0', port=5000, threads=1)
    else:
        print("in dev")
        app.run(debug=True)