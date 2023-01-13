from tkinter import *
from tkinter import ttk, messagebox
import pandas as pd
from tkcalendar import Calendar

df = pd.read_csv("C:/Users/User/Desktop/test.csv")
df_new = pd.read_csv("C:/Users/User/Desktop/database.csv")


root = Tk()
root.title('WAYBILL RECORDING APP')
root.iconbitmap('C:/Users/User/Downloads/car.ico')
root.geometry("800x400")
root.configure(bg='#F3FAF9')
root.resizable(height=False, width=False)
upload_button_image = PhotoImage(file='C:/Users/User/Desktop/upload.png')

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
            pass
    else:
        box2['values'] = ['']


# creating searchable combobox (box1)
def searchbox3():
    value = box3.get()
    if value == '':
        box3['values'] = df['dqn'].dropna().tolist()
    else:
        data = []
        for item in df['dqn'].dropna().tolist():
            if value.lower() in item.lower():
                data.append(item)
        box3['values'] = data


# Button is checking if Combo Boxes and Entry are empty
# and if start date greater than end date
def btn_click():
    if (not box1.get() or not box2.get() or not box3.get() or not entry.get() or not entry_hour.get()
            or int(cal1.get_date().split("/")[0]) > int(cal2.get_date().split("/")[0])):
        messagebox.showerror("ERROR", "Data entered incorrectly")
    else:
        dqn_index = df[df['dqn'] == box3.get()].index.item()
        day = (int(cal2.get_date().split("/")[0]) - int(cal1.get_date().split("/")[0])) + 1
        messagebox.showinfo("SUCCESS", "Data entered correctly")
        df_new.loc[df_new.shape[0]] = [box1.get(), box2.get(), df['marka'].values[dqn_index],
                                       box3.get(), entry.get(), cal1.get_date(), cal2.get_date(),
                                       entry_hour.get(), day]
        df_new.to_csv("C:/Users/User/Desktop/database.csv", index=False)
        box1.set('')
        box2.set('')
        box3.set('')
        entry_hour.delete(0, 'end')
        entry.delete(0, 'end')


# creating first Combobox
box1_name = Label(root, text="organization", fg='#FF0000', font=('Helvetica', 10, 'bold'))
box1_name.place(x=325, y=-4)
box1 = ttk.Combobox(root, postcommand=searchbox1)
box1.pack(pady=15)

# creating second Combobox
box2_name = Label(root, text="sub_organization", fg='#FF0000', font=('Helvetica', 10, 'bold'))
box2_name.place(x=325, y=48)
box2 = ttk.Combobox(root, postcommand=searchbox2)
box2.pack(pady=15)

# creating third Combobox
box3_name = Label(root, text="car_number", fg='#FF0000', font=('Helvetica', 10, 'bold'))
box3_name.place(x=325, y=99)
box3 = ttk.Combobox(root, postcommand=searchbox3)
box3.pack(pady=15)

# creating Entry widget
entry_hour_label = Label(root, text="hours", fg='#FF0000', font=('Helvetica', 10, 'bold'))
entry_hour_label.place(x=363, y=160)
entry_hour = Entry(root, bd=5, width=10, justify='center')
entry_hour.pack(pady=25)

# creating Entry widget
entry_label = Label(root, text="WB_number", fg='#FF0000', font=('Helvetica', 10, 'bold'))
entry_label.place(x=325, y=212)
entry = Entry(root, bd=5, width=22, justify='center')
entry.pack()

# add "From date" Calendar
cal1_label = Label(root, text="from_date", fg='#FF0000', font=('Helvetica', 10, 'bold'))
cal1_label.place(x=34, y=64)
cal1 = Calendar(root, selectmode='day', day=1, date_pattern='d/m/y')
cal1.place(relx=0.2, rely=0.44, anchor=CENTER)

# add "To date" Calendar
cal2_label = Label(root, text="to_date", fg='#FF0000', font=('Helvetica', 10, 'bold'))
cal2_label.place(x=512, y=64)
cal2 = Calendar(root, selectmode='day', day=1, date_pattern='d/m/y')
cal2.place(relx=0.8, rely=0.44, anchor=CENTER)

# creating Button widget
btn = Button(root, image=upload_button_image, bd=0, bg='#F3FAF9', activebackground="#F3FAF9", command=btn_click)
btn.pack(pady=40)

root.mainloop() 
