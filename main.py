from tkinter import *
import requests

screen = Tk()
screen.title("Crypto Dashboard")
screen.minsize(500, 500)
screen.config(padx=50, pady=50)
FONT = ("Verdana",20,"normal")

def get_crypto_data():
    response = requests.get(url="https://raw.githubusercontent.com/atilsamancioglu/K21-JSONDataSet/master/crypto.json")
    return response.json()




search_title = Label(text="Search Crypto: ")
search_title.place(x=50,y=100)

search_entry = Entry(width=25)
search_entry.place(x=150,y=100)


def button_clicked():
    search_crypto = search_entry.get()
    crypto_response = get_crypto_data()
    for crypto in crypto_response:
        if crypto["currency"] == search_crypto:
            print(crypto["currency"],": ",crypto["price"])
            break




search_button = Button(text="Search",command=button_clicked)
search_button.place(x=175,y=150)


crypto_message = Label()
crypto_message.place(x=175,y=50)







screen.mainloop()
