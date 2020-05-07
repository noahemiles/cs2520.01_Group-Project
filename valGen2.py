import csv
import random
import time
from bs4 import BeautifulSoup
import urllib.request
import pandas as pd
import requests
import os
from datetime import datetime


stockLabel = input("Enter Stock Label: ").upper()

def getPrice():
    page = urllib.request.urlopen("http://www.finance.yahoo.com/quote/"+stockLabel)
    pageText = page.read()
    decodedPageText = pageText.decode("utf-8")
    yahooQuery = "<span class="
    find = lambda sentence, qry: sentence[sentence.find(qry):sentence.find(qry)+97] if qry in sentence else -1
    htmlLineWithPrice = find(decodedPageText, yahooQuery)
    #parse htmlLineWithPrice to only have price
    stockPrice = float(htmlLineWithPrice.split(" ")[-1].split(">")[1].split("<")[0])
    return stockPrice


class generator:
    def __init__ (self, fieldname):
        with open('data.csv', 'w', newline='') as csv_file:
            csv_writer = csv.writer(csv_file)
    def collect(self, fieldname):
        total_1 = getPrice()
        while True:
            with open('data.csv', 'a') as csv_file:
                total_1 = getPrice()
                today = datetime.now()
                x_value = round(today.hour+today.minute/60.0,2)
                print(x_value, total_1)
                csv_writer = csv.writer(csv_file)
                csv_writer.writerow([x_value, total_1])
            time.sleep(60)

fieldnames = ["x_value", "total_1"]
g = generator(fieldnames)
g.collect(fieldnames)

