import re
import traceback

import requests
from bs4 import BeautifulSoup

# 定向爬取股票数据

def getHTMLText(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36'}
    try:
        r = requests.get(url, headers=headers)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        print('读取失败')


def getStockList(stocklst: list, url):
    html = getHTMLText(url)
    soup = BeautifulSoup(html, 'html.parser')
    div = soup.find('div', class_='quotebody')  # 注意 'class' 是python 的关键字,直接用会报错，需改用 'class_'
    a = div.find_all('a')
    for i in a:
        # 注意这里的 a 标签不仅有记录股票代码的标签，还有其他类型的 a 标签，
        # 因此不是所有的 a 标签都符合正则表达式的方式，会出现错误和异常，
        # 用 try...continue 可以过滤掉这些异常
        try:
            href = i.attrs['href']
            stocklst.append(re.findall(r'[s][hz]\d{6}', href)[0])
        except:
            continue


def getStockInfo(stocklst:list, stockurl, fpath):
    count = 0   # 进度计数
    for i in stocklst:
        url = stockurl + i[-6:] + '/index.shtml'
        html = getHTMLText(url)

        try:
            if html == '':
                continue
            infoDict = {}
            soup = BeautifulSoup(html, 'html.parser')
            li = soup.find('li', class_='name')
            name = li.find('a').text
            infoDict.update({'股票名称': name.strip(), '股票编号': i})
            with open(fpath, 'a', encoding='utf-8') as f:
                f.write(str(infoDict) + '\n')
                count += 1
                print('\r当前进度：{:.2f}%'.format(count*100/len(stocklst)), end='')  # 动态进度条显示

        except:
            traceback.print_exc()
            count += 1
            print('\r当前进度：{:.2f}%'.format(count * 100 / len(stocklst)), end='')
            continue


def main():
    stock_list_url = 'http://quote.eastmoney.com/stocklist.Html'    # 东方财富
    stock_info_url = 'https://q.stock.sohu.com/cn/'     # 搜狐财经
    output_file = 'E://SouhuStockInfo.txt'
    stocklst = []
    getStockList(stocklst, stock_list_url)
    getStockInfo(stocklst, stock_info_url, output_file)


main()
