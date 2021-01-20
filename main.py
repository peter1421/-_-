import requests
from bs4 import BeautifulSoup
import json
import tkinter as tk
import tkinter.font as tkFont
class shop_data:
    def __init__(self,url):
        self.headers = {'User-Agent': 'Googlebot','From': 'abcde12345326@gmail.com'}
        self.url=url
        self.root=None
        self.content=None
        self.title=None
        self.price=None
        self.priceCurrency=None
    def get_data(self):
        response=requests.get(self.url,headers=self.headers,allow_redirects=True)
        self.root = BeautifulSoup(response.text, "html.parser")  
    def get_content(self):
        self.content=self.root.find_all('script', {'type':'application/ld+json'})[-1].prettify()
        self.content=json.loads(self.content[50:-10])
    def get(self):
        self.get_data()
        self.get_content()
    def get_title(self):
        self.title=self.content["name"]
        return self.title
    def get_price(self):
        self.price=self.content["offers"]["price"]
        return self.price
    def get_priceCurrency(self):
        self.priceCurrency=self.content["offers"]["priceCurrency"]
        return self.priceCurrency
    def show(self):
        print(self.get_title(),"=>",self.get_price(),self.get_priceCurrency())
        try:
            final=self.get_title(),"=>",self.get_price(),self.get_priceCurrency()
            print(final)
            final_frame = tk.Frame(window).pack(side=tk.TOP)
            final_label= tk.Label(final_frame, text=final,font=fontStyle1).pack()
        except:
            print("no")

def new_data():
    url=str(input_entry.get())
    global data1
    data1=shop_data(url)
    data1.get()
    data1.show()


data1=shop_data("https://shopee.tw/product/124885008/9610930766/")
data1.get()
data1.show()



window = tk.Tk()
imLabel=tk.Label(window)
window.title('價格追蹤器')
window.geometry('800x600')
window.configure(background='orange')
fontStyle1 = tkFont.Font(size=20)
fontStyle2 = tkFont.Font(size=10)
header_label = tk.Label(window, text='價格追蹤器', font=fontStyle1).pack()
#輸入網址
input_frame = tk.Frame(window).pack(side=tk.TOP)
input_label = tk.Label(input_frame, text='請輸入網址').pack(side=tk.TOP)
input_entry= tk.Entry(input_frame).pack(side=tk.TOP)

Data_frame = tk.Frame(window).pack(side=tk.TOP)
Data_label = tk.Button(Data_frame, text="確認",command=data1.get,font=fontStyle2).pack()

# 更新匯率
UpData_frame = tk.Frame(window).pack(side=tk.TOP)
UpData_label = tk.Button(UpData_frame, text="更新匯率",command=data1.get,font=fontStyle2).pack()


#開始計算
cal_frame=tk.Frame(window).pack(side=tk.LEFT)
cal_label  = tk.Button(UpData_frame, text="輸出",command=data1.show,font=fontStyle2).pack()
#cal_label = tk.Button(cal_frame, text="開始計算",command=lambda :cal(now_num,change_num),font=fontStyle2).pack()

result_label = tk.Label(window).pack()
window.mainloop()
