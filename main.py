from tkinter import *
from tkinter import ttk
import pandas as pd

df = pd.read_csv("C:/Users/User/Desktop/test.csv")

root = Tk()
root.title('Codemy.com - Dependent Dropdowns')
root.iconbitmap('C:/Users/User/Downloads/car.ico')
root.geometry("800x400")

comp_lst = df.companies.dropna().tolist()


# creating searchable combobox (box1)
def searchbox1():
    value = box1.get()
    if value == '':
        box1['values'] = comp_lst
    else:
        data = []
        for item in comp_lst:
            if value.lower() in item.lower():
                data.append(item)
        box1['values'] = data


# creating searchable combobox (box2)
def searchbox2():
    if box1.get() != '':
        try:
            box2['values'] = df[box1.get()].dropna().tolist()
            value = box2.get()
            data = []
            for item in df[box1.get()].dropna().tolist():
                if value.lower() in item.lower():
                    data.append(item)
            box2['values'] = data
        except KeyError:
            print('KeyError')
            pass
    else:
        box2['values'] = ['']


# creating first Combobox
box1 = ttk.Combobox(root, postcommand=searchbox1)
box1.pack(pady=20)


# creating second Combobox
box2 = ttk.Combobox(root, postcommand=searchbox2)
box2.pack(pady=20)


root.mainloop()
