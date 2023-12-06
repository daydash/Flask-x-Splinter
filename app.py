from selenium import webdriver
from splinter import Browser
import time
from flask import Flask, render_template, render_template_string
# ,request, jsonify
from waitress import serve
from flask_cors import CORS
from selenium.webdriver.chrome.options import Options
import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

app = Flask(__name__)
cors = CORS(app)

@app.route("/")
# @cross_origin()
def hello_world():
    logging.info("HELLO, from /")
    return "<p>Hello, World!!</p>"

@app.route("/search3")
def search3():
    script_to_inject = """
        <script type="text/javascript" src="https://cdn.jsdelivr.net/npm/pyodide@0.24.1/pyodide.min.js"></script>
        <script type="text/javascript">
        console.log("Before using languagePluginLoader");
        loadPyodide({ indexURL: "https://cdn.jsdelivr.net/pyodide/v0.18.0/full" }).then((pyodide) => {
            console.log("inside lang")
            globalThis.pyodide = pyodide 
            pyodide.loadPackage(['selenium','splinter']).then(() => {
            const result = pyodide.runPython(`
                from selenium import webdriver
                import time
                from selenium.webdriver.chrome.options import Options
                import logging

                try:
                    
                    chrome_options = Options()
                    driver = webdriver.Chrome(options=chrome_options)
                    data = driver.get('https://www.google.com')
                

                    search_box = driver.find_element('name','q')
                
                    search_box.send_keys("chatgpt")
                 
                    search_box.submit()
     
                    time.sleep(5)
                except:
                    logging.warning('in expect\n')
            `);
            console.log(result);
            });
        });
        console.log("After using languagePluginLoader");
        </script>
    """
    return render_template_string("<html><body>{{ script_to_inject | safe}}</body></html>", script_to_inject=script_to_inject)



@app.route("/search2")
def search2():
    try:
        logging.warning("search2 hitted\n")
        chrome_options = Options()
        logging.warning("search2 1\n")
        # chrome_options.add_argument('--headless')
        logging.warning("search2 2\n")
        # chrome_options.add_argument('--disable-gpu')
        driver = webdriver.Chrome(options=chrome_options)
        logging.warning("search2 3\n")
        # driver = webdriver.Chrome()
        data = driver.get("https://www.google.com")
        logging.warning("search2 4\n")

        search_box = driver.find_element("name","q")
        logging.warning("search2 5\n")
        search_box.send_keys("chatgpt")
        logging.warning("search2 6\n")
        search_box.submit()
        logging.warning("search2 7\n")
        time.sleep(5)
    except:
        logging.warning("in expect\n")
   
    return "hello form search2 "

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
        logging.info("Yes, the official website was found!")
    else:
        logging.info("No, it wasn't found... We need to improve our SEO techniques")

    browser.quit()

    return "hello from search route"
    # return render_template('index.html')

# @app.route("/loginToWW", methods=["POST"])
# @cross_origin()
# def login():
#     username = request.json['username']
#     password = request.json['password']

#     logging.info(username, password)

#     try:
#         # options = webdriver.ChromeOptions()
#         # options.add_argument('--headless') 
#         # options.add_argument('--disable-gpu')
#         # driver = webdriver.Chrome(options=options)

#         browser = Browser()
#         browser.visit('https://vaishu-15.github.io/WealthWise/')
#     except Exception as error:
#         logging.info("Error in Browser instance ->\n", error)

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

mode = "dev"

if __name__ == "__main__":
    if mode == "prod":
        logging.critical("in prod")
        serve(app, host='0.0.0.0', port=5000, threads=1)
    else:
        logging.critical("in dev")
        app.run(debug=True)