import requests
from bs4 import BeautifulSoup
import pandas as pd 
import datetime

def bse_stock_price():
    url = "https://in.finance.yahoo.com/quote/%5EBSESN?p=^BSESN"
    r = requests.get(url)
    web_content = BeautifulSoup(r.text,'lxml')
    web_content = web_content.find('div',{"class" : "My(6px) Pos(r) smartphone_Mt(6px)"})
    web_content = web_content.find('span').text


    if web_content ==[]:
        web_content = '99999'

    return web_content

h = ["data","price"]
for step in range(1,101):
    price = []
    col = []
    time_stamp = datetime.datetime.now()
    time_stamp = time_stamp.strftime("%Y-%M-%D %H:%M:%S")
    price.append(bse_stock_price())
    col = [time_stamp]
    col.extend(price)
    df = pd.DataFrame(col)
    df = df.T 
    df.to_csv("/root/Documents/Other_Works/Experiments_101/Exp_6/bse_stock.csv",mode="a",header=h)
    print(col)
