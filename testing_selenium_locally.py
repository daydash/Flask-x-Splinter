from selenium import webdriver
import logging, time
# driver = webdriver.Chrome()
# driver.get("https://www.google.com")

# search_box = driver.find_element("name","q")
# search_box.send_keys("chatgpt")
# search_box.submit()

from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.ui import Select

import numpy as np
a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
print(a[0])

logging.warning("search2 hitted\n")
# chrome_options = Options()
logging.warning("search2 1\n")
# chrome_options.add_argument('--headless')
logging.warning("search2 2\n")
# chrome_options.add_argument('--disable-gpu')
# driver = webdriver.Chrome(options=chrome_options)
# driver = webdriver.Chrome("D:/SeleniumServer/chromedriver.exe")
# driver = webdriver.Chrome(ChromeDriverManager().install())
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