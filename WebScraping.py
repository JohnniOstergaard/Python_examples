#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#Description ===================================================================
#   This code was written following a tutorial* from PythonProgramming.net**
#   then modified for used as example and reminder of how to build a Web Scraper.
#   *Title:         Web scraping and parsing with Beautiful Soup
#   **URL:          https://pythonprogramming.net/introduction-scraping-parsing-beautiful-soup-tutorial/
#Information ===================================================================
#   File name:      WebScraping.py
#   Author:         Johnni Østergaard
#   Copyright:      (c) 2017 Johnni Østergaard
#   Credits         PythonProgramming | https://pythonprogramming.net/
#   License:        MIT License
#   Interpreter:    Python 3.5.2
#Progress ======================================================================
#   Status:         Development
#   Version:        1.0.0        | Major.minor.patch
#   Created:        14-03-2017
#   Modified:       16-03-2017   | Improved readability
#===============================================================================

#Standard modules
import urllib.request                   #URLopening module
import sys                              #System specific parameters and functions module
#Third party modules
import bs4                              #WebScraping module - Beautiful Soup 4
#from PyQt4.QtGui import QApplication    #App flow and setting class - GUI module
#from PyQt4.QtCore import QUrl           #URL interface class - Base module
#from PyQt4.QtWebKit import QWebPage     #Web view/edit class - WebKit module
#Info about modules
    #bs4 website:       https://www.crummy.com/software/BeautifulSoup/bs4/doc/#
    #PyQt4 website:     https://riverbankcomputing.com/software/pyqt/intro
    #PyQt4 note:        PyQt4 is easy to work with and has less dependencys than PyQt5

#Function definitions ==========================================================
sauce = urllib.request.urlopen('https://pythonprogramming.net/parsememcparseface/').read()
soup = bs4.BeautifulSoup(sauce,'lxml')

def get_text(case):
    if(case == 1):      print(sauce)                #print page whitout format
    elif(case == 2):    print(soup)                 #print page using the LXML format
    elif(case == 3):    print(soup.title)           #print the page title as: <title>title_string</title>
    elif(case == 4):    print(soup.title.name)      #print name of the title tag
    elif(case == 5):    print(soup.title.string)    #print the string of the title tag
    elif(case == 6):    print(soup.title.text)      #print the string of the title tag
    elif(case == 7):    print(soup.p)               #print first paragraph tag
    elif(case == 8):    print(soup.find_all('p'))   #print all paragraph tags
    elif(case == 9):    print(soup.get_text())      #print all text on page including pre tags: <pre> </pre>
    elif(case >= 10 and case <= 12):
        for paragraph in soup.find_all('p'):
            if(case == 10):     print(paragraph)            #print all paragraph tags one by one
            elif(case == 11):   print(paragraph.string)     #print all paragraph strings one by one
            elif(case == 12):   print(paragraph.text)       #print all paragraph text one by one
            #Note case11: .string do not work with child tags: <span> </span> or <strong> </strong>
            #Note case12: returns all text, including stuff like: cancel, login, sign up, ...
    elif(case == 13):
        body = soup.body
        for paragraph in body.find_all('p'):
            print(paragraph.text)                   #print all paragraphs in the page body
    elif(case == 14):
        for div in soup.find_all('div'):
            print(div.text)                         #print all text from div tags
    elif(case == 15):
        for div in soup.find_all('div', class_='body'):
            print(div.text)                         #print all text between div tags

def get_url(case):
    for url in soup.find_all('a'):
        if(case == 1):
            print(url)                              #print all url tags from the page
        elif(case == 2):
            print(url.text)                         #print all url text from the page
        elif(case == 3):
            print(url.get('href'))                  #print all url links from the page
        elif(case == 4):
            print(soup.nav)                         #print all between Nav tags
        elif(case == 5):
            nav = soup.nav
            for url in nav.find_all('a'):
                print(url.get('href'))              #print all url in the Navigating tags
                    #The some of the URLs can be the same if the page has code for a mobil view

def get_xml():                                      #XML pages offen used as sitemaps
    sauce = urllib.request.urlopen('https://pythonprogramming.net/sitemap.xml').read()
    soup = bs4.BeautifulSoup(sauce,'xml')
    print(soup)                                     #print all from page
    for url in soup.find_all('loc'):
        print(url.text)                             #print all text inbetween <loc> tags

def get_table(case):
    if(case == 1):
        table = soup.table
        print(table)                                #print all table tags
            #note: <tr> = table row, <td> = table data, <th> = table header
    elif(case == 2):
        table = soup.find('table')
        print(table)                                #print all table tags
    elif(case == 3):
        table = soup.find('table')
        table_rows = table.find_all('tr')
        for tr in table_rows:
            td = tr.find_all('td')
            row = [i.text for i in td]
            print(row)                              #print all table data
                #The first row is the table header and will show up as empty

def run_js():                                       # Scraping info from a dynamic javascrip
    """
    class Client(QWebPage):
        def __init__(self, url):
            self.app = QApplication(sys.argv)
            QWebPage.__init__(self)
            self.loadFinished.connect(self.on_page_load)
            self.mainFrame().load(QUrl(url))
            self.app.exec_()

        def on_page_load(self):
            self.app.quit()

    url = 'https://pythonprogramming.net/parsememcparseface/'
    client_response = Client(url)
    source = client_response.mainFrame().toHtml()
    soup = bs4.BeautifulSoup(sauce,'lxml')
    js_test = soup.find('p', class_='jstest')
    print(js_test.text)     #print only the tag text, not the text form the script!
        #In order to run the java script, we make a browser client that can run it.
    """
#Main code =====================================================================
#get_text(15)
#get_url(5)
#get_xml()
get_table(3)
