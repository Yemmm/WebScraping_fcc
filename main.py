# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

# Web Scraping with Python - Beautiful Soup Crash Course
# https://youtu.be/XVv6mJpFOb0

# Install the following:
# pip install beautifulsoup4
# pip install lxml

from bs4 import BeautifulSoup

with open('home.html', 'r') as html_file:
    content = html_file.read()

    soup = BeautifulSoup(content, 'lxml')
    # tags = soup.find('h1') #finds first element instance

    # p_html_tags = soup.find_all('p')
    # for p in p_html_tags:
    #     print(p.text)

    div_tags = soup.find_all('div', class_='test')
    for div in div_tags:
        h1 = div.h1.text
        h1_modified = h1.split()[-1]
        print(h1_modified)