from selenium import webdriver
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from bs4 import BeautifulSoup
import webbrowser


def parseForHref(html):
    html_soup: BeautifulSoup = BeautifulSoup(html, 'html.parser')
    return html_soup.find(id="dlbutton")['href']


def getResourceLink(pageLink, resourceLink):
    link1 = pageLink.split('v/', 1)[0][:-1]
    return link1 + resourceLink


file = open("links.txt", "r")
lines = file.readlines()
options = FirefoxOptions()
options.add_argument("--headless")
driver = webdriver.Firefox(options=options)

for line in lines:
    driver.get(line)
    ref = parseForHref(driver.execute_script(
        "return document.body.innerHTML;"))
    webbrowser.open(getResourceLink(line, ref))
