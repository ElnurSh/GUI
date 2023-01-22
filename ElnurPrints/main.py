# if your computer is on a local network but for technical reasons
# you do not have direct access to a printer that is connected to 
# another computer from a local network, 
# then perhaps the solution would be to install this utility
# on a local computer with a printer
# *your computer and the computer with the printer must have access to an empty network folder

import os
from tkinter import *
from time import sleep


root = Tk()
root.title('ElnurPrints')
root.iconbitmap('icon.ico')
root.geometry("200x300")
root.configure(bg='black')
root.resizable(False, False)
scanning = True


def printing():
    try:
        if scanning:
            text.configure(text='Searching...')
            dir_list = os.listdir(r"\\192.168.1.118\empty")

            if not dir_list:
                pass
            else:
                for file in dir_list:
                    os.startfile(fr"\\192.168.1.118\empty\{file}", "print")
                    sleep(20)
                    os.remove(fr"\\192.168.1.118\empty\{file}")
    except:
        text.configure(text='ERROR')
        pass
    root.after(3000, printing)


def click_off():
    text.configure(text='')
    photo.configure(file='photo_OFF.png')
    button.configure(command=click_on)
    global scanning
    scanning = False


def click_on():
    text.configure(text='Axtarır...')
    photo.configure(file='photo_ON.png')
    button.configure(command=click_off)
    global scanning
    scanning = True
    printing()


photo = PhotoImage(file=r'photo_OFF.png')
button = Button(root, image=photo, border=0, bg='black', command=click_on, activebackground='black')
button.place(x=30, y=180)

text = Label(root, text='', border=0, bg='black', fg='yellow', font=('Tahoma bold', 22))
text.place(x=60, y=60)

if __name__ == '__main__':
    root.mainloop()
