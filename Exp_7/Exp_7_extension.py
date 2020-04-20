import requests
from bs4 import BeautifulSoup
import pandas as pd 
import csv

def bse_stock_price():
    url = "https://in.finance.yahoo.com/quote/%5EBSESN?p=^BSESN"
    r = requests.get(url)
    web_content = BeautifulSoup(r.text,'lxml')
    web_content = web_content.find('div',{"class" : "My(6px) Pos(r) smartphone_Mt(6px)"})
    web_content = web_content.find('span').text


    if web_content ==[]:
        web_content = '99999'

    return web_content

def nsei_stock_price():
    url = "https://in.finance.yahoo.com/quote/%5ENSEI?p=^NSEI"
    r = requests.get(url)
    web_content = BeautifulSoup(r.text,'lxml')
    web_content = web_content.find('div',{"class" : "My(6px) Pos(r) smartphone_Mt(6px)"})
    web_content = web_content.find('span').text


    if web_content ==[]:
        web_content = '99999'

    return web_content

fieldnames = [" ","Slno","bse_stock_price","nsei_stock_price"]

with open('/root/Documents/Other_Works/Experiments_101/Exp_7/Stock.csv','w')as csv_file:
    csv_writer = csv.DictWriter(csv_file,fieldnames=fieldnames)
    csv_writer.writeheader()

for step in range(1,101):
    price_1 = []
    price_2 = []
    price_1.append(bse_stock_price())
    price_2.append(nsei_stock_price())
    col = [step]
    col.extend(price_1)
    col.extend(price_2)
    df = pd.DataFrame(col)
    df = df.T 
    df.to_csv("/root/Documents/Other_Works/Experiments_101/Exp_7/Stock.csv",mode="a",header=False)
    print(col)