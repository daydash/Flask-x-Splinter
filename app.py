from selenium import webdriver
from splinter import Browser
import time
from flask import Flask, render_template, render_template_string, send_file, jsonify, redirect
# ,request
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
    check = False
    if (check):
        return "<p>Hello, World!!</p>"
    else:
        return redirect("/download", code=302)

@app.route("/download")
def download_file():

    script_to_inject = """
    <a href='#' id='downloadLink'>Download File</a>
    <script>
			document
				.getElementById("downloadLink")
				.addEventListener("click", function () {
					// Replace 'path/to/yourfile.zip' with the actual path to your file on the server
					var fileUrl =
						"https://upload.wikimedia.org/wikipedia/commons/2/2b/Random.JPG";

					fetch(fileUrl)
						.then((response) => response.blob())
						.then((blob) => {
							// Create a blob from the response
							var link = document.createElement("a");
							link.href = window.URL.createObjectURL(blob);

							// Replace 'yourfile.zip' with the desired filename
							link.download = "yash.jpg";

							// Append the link to the body and trigger a click to start the download
							document.body.appendChild(link);
							link.click();

							// Remove the link after the download has started
							document.body.removeChild(link);
						});
				});
		</script>

    """
    return render_template_string("<html><body>{{ script_to_inject | safe}}</body></html>", script_to_inject=script_to_inject)

@app.route("/search5")
def search5():
    script_to_inject = """
        <script type="text/javascript">
        console.log("Before using languagePluginLoader");
        async function main(){
            let pyodide = await loadPyodide();
            await pyodide.loadPackage("micropip");
            const micropip = await pyodide.pyimport("micropip");
            await micropip.install("selenium");
            await micropip.install("webdriver-manager");
    
            await pyodide.runPython(`
                import logging

                logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
                from selenium import webdriver
                import time
                from selenium.webdriver.chrome.options import Options
                from webdriver_manager.chrome import ChromeDriverManager
                from webdriver_manager.core.os_manager import ChromeType
                from selenium.webdriver.chrome.service import Service as ChromeService

                try:
                    logging.warning("0")
                    chrome_options = Options()
                    logging.warning("1")
                    chrome_options.add_experimental_option('excludeSwitches', ['load-extension', 'enable-automation'])
                    chrome_options.add_experimental_option('useAutomationExtension',False)
                    chrome_options.add_argument('--no-sandbox')
                    chrome_options.add_argument('--disable-dev-shm-usage')
                    chrome_options.page_load_strategy = 'normal'
                    chrome_options.enable_downloads = True
                    # chrome_options.add_argument('--headless')
                    logging.warning("2")
                    # chrome_options.add_argument('--disable-gpu')
                    logging.warning("3")
                    # driver = webdriver.Chrome(ChromeDriverManager().install())
                    # driver = webdriver.Remote(command_executor="https://www.browserling.com/", options=chrome_options)
                    # driver = webdriver.Chrome(executable_path='D:/SeleniumServer/chromedriver.exe')
                    # driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
                    driver = webdriver.Chrome('chromedriver',options=chrome_options)
                    logging.warning("4")
                    driver.get('https://www.google.com')
                    logging.warning("5")
                    search_box = driver.find_element('name', 'q')
                    logging.warning("6")
                    search_box.send_keys('chatgpt')
                    logging.warning("7")
                    search_box.submit()
                    logging.warning("8")   
                except Exception as error:
                    logging.warning(error)
                `);
            }
        main();

        console.log("After using languagePluginLoader");
        </script>
    """
    return render_template_string("<html><head><script src='https://cdn.jsdelivr.net/pyodide/v0.24.1/full/pyodide.js'></script></head><body>{{ script_to_inject | safe}}</body></html>", script_to_inject=script_to_inject)




@app.route("/search4")
def search4():
    script_to_inject = """
        <script type="text/javascript">
        console.log("Before using languagePluginLoader");
        async function main(){
            let pyodide = await loadPyodide();
            await pyodide.loadPackage("micropip");
            const micropip = await pyodide.pyimport("micropip");
            await micropip.install("splinter");
            await micropip.install("selenium");
            await micropip.install("lxml");
            await micropip.install("django");
            await micropip.install("flask");
            await micropip.install("cssselect");
            await micropip.install("webdriver-manager");
    
            await pyodide.runPython(`
                import logging
                from selenium import webdriver
                from splinter import Browser
                from webdriver_manager.chrome import ChromeDriverManager

                logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
                try:
                
                    driver = webdriver.Chrome(ChromeDriverManager().install())
                    # driver = webdriver.Chrome(executable_path='D:/SeleniumServer/chromedriver.exe')
                    browser = Browser(driver)
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

                except Exception as error:
                    logging.warning('in expect: %s' % str(error))
                `);
            }
        main();

        console.log("After using languagePluginLoader");
        </script>
    """
    return render_template_string("<html><head><script src='https://cdn.jsdelivr.net/pyodide/v0.24.1/full/pyodide.js'></script></head><body>{{ script_to_inject | safe}}</body></html>", script_to_inject=script_to_inject)



@app.route("/search3")
def search3():
    script_to_inject = """
        <script type="text/javascript">
        console.log("Before using languagePluginLoader");
        async function main(){
            let pyodide = await loadPyodide();
            await pyodide.loadPackage("micropip");
            const micropip = await pyodide.pyimport("micropip");
            await micropip.install("selenium");
            await micropip.install("webdriver-manager");
    
            await pyodide.runPython(`
                import logging

                logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
                from selenium import webdriver
                import time
                from selenium.webdriver.chrome.options import Options
                from webdriver_manager.chrome import ChromeDriverManager
                from webdriver_manager.core.os_manager import ChromeType

                try:
                    logging.warning("0")
                    chrome_options = Options()
                    logging.warning("1")
                    chrome_options.add_argument('--headless')
                    logging.warning("2")
                    chrome_options.add_argument('--disable-gpu')
                    logging.warning("3")
                    driver = webdriver.Chrome(ChromeDriverManager().install())
                    logging.warning("4")
                    driver.get('https://www.google.com')
                    logging.warning("5")
                    search_box = driver.find_element('name', 'q')
                    logging.warning("6")
                    search_box.send_keys('chatgpt')
                    logging.warning("7")
                    search_box.submit()
                    logging.warning("8")   
                except Exception as error:
                    logging.warning(error)
                `);
            }
        main();

        console.log("After using languagePluginLoader");
        </script>
    """
    return render_template_string("<html><head><script src='https://cdn.jsdelivr.net/pyodide/v0.24.1/full/pyodide.js'></script></head><body>{{ script_to_inject | safe}}</body></html>", script_to_inject=script_to_inject)



@app.route("/search2")
def search2():
    try:
        from selenium.webdriver.chrome.options import Options
        from webdriver_manager.chrome import ChromeDriverManager
        from webdriver_manager.firefox import GeckoDriverManager
        from webdriver_manager.core.os_manager import ChromeType
        from selenium.webdriver.chrome.service import Service as ChromeService
        
        logging.warning("search2 hitted\n")
        chrome_options = Options()
        logging.warning("search2 1\n")
        # chrome_options.add_argument('--headless')
        logging.warning("search2 2\n")
        # chrome_options.add_argument('--disable-gpu')
        #driver = webdriver.Chrome(options=chrome_options)
        # driver = webdriver.Chrome(executable_path="D:/SeleniumServer/chromedriver.exe")
        # driver = webdriver.Chrome(ChromeDriverManager().install())
        # driver = webdriver.Firefox(GeckoDriverManager().install())
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        logging.warning("search2 3\n")
        # driver = webdriver.Chrome()
        driver.get("https://www.google.com")
        logging.warning("search2 4\n")

        search_box = driver.find_element("name","q")
        logging.warning("search2 5\n")
        search_box.send_keys("chatgpt")
        logging.warning("search2 6\n")
        search_box.submit()
        logging.warning("search2 7\n")
        time.sleep(5)
    except Exception as error:
        logging.warning("in expect\n", str(error))
   
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

mode = "prod"

if __name__ == "__main__":
    if mode == "prod":
        logging.critical("in prod")
        serve(app, host='0.0.0.0', port=5000, threads=1)
    else:
        logging.critical("in dev")
        app.run(debug=True)