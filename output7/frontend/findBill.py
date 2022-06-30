import tkinter
from tkinter import messagebox
from tkinter import *
import operator
from numpy import delete, insert
from baseInitialization import UiFields
from database import findBillData, findBillTotal, findBillDataByfilter, bill_delete
from datetime import datetime
from common import date_to_string
import os

name = 50
si = 10
bill_no = 10
buttons = []
delete_buttons = []
ornament = 70
total = 15
text: Frame
h: Scrollbar
v: Scrollbar

u = UiFields()
# ======================================================================================================
def convert_to_string(result):
    ret = ''
    for i in range(len(result)-2):
        if type(result[i]) == datetime:
            ret += date_to_string(result[i])
            
        elif type(result[i]) == int:
            k = 10 - len(str(result[i]))
            ret += str(result[i])
            while k:
                k = k-1
                ret += ' '
        else:
            k = 50 - len(result[i])
            ret += str(result[i])
            while k:
                k = k-1
                ret += ' '
        ret += '      '
    return ret


def openBill(m, l):
    buttons[m].config(bg='#'+u.blue)
    if os.path.exists(l):
        try:
            os.system("start EXCEL.EXE "+l)
        except Exception as e:
            print('There is a error in opening the file :{0}'.format(e))
            messagebox.showerror("Error", 'There is a error in opening the file : {0}'.format(e))
    else:
        print('File Not Found')
        messagebox.showerror("Not Found", 'File Is Not Found')
        
def delete_bill(m, l):
    if messagebox.askokcancel('Sure', 'Do You Want to delete??'):
        delete_buttons[m].config(bg='#'+u.blue)
        print(m,l)
        bill_data = l.split('\\')
        bill_no = bill_data[len(bill_data)-1].split('.')[0]
        print(bill_no)
        bill_delete(bill_no)
    
        
def noDataFound(F: Frame):
    global buttons, text, h, v
    buttons= []
    text = Text(F, width=50, height=35, wrap=NONE,
            xscrollcommand=h.set,
            yscrollcommand=v.set)
    text.insert('1.0', 'No Bill Found')
    Desired_font = tkinter.font.Font( family = "Times New Romman", 
                                 size = 20, 
                                 weight = "bold")
    text.configure(font=Desired_font)

    text.pack(side=TOP, fill=X)
    text.config(state=DISABLED)

    
def insertBillData(F: Frame, result):
    global delete_buttons, buttons, text, h, v
    buttons= [] 
    delete_buttons = []
    h = Scrollbar(F, orient='horizontal')
    h.pack(side=BOTTOM, fill=X)
    v = Scrollbar(F)
    v.pack(side=RIGHT, fill=Y)
    text = Text(F, width=50, height=35, wrap=NONE,
            xscrollcommand=h.set,
            yscrollcommand=v.set)

    for i in range(0, len(result)):
        bill_location = result[i][len(result[i])-2]
        button = Button(text, text=convert_to_string(result[i]),
                        font=('times new romman',10), command=lambda m=i,l=bill_location: openBill(m, l), bg='#'+u.green, fg='white')
        delete_button = Button(text, text='DELETE',
                                font=('times new romman',10), command=lambda m=i,l=bill_location: delete_bill(m, l), bg='#'+u.red, fg='white')
        buttons.append(button)
        delete_buttons.append(delete_button)
        
    insertButtons(text, buttons, delete_buttons)
    text.pack(side=TOP, fill=X)
    text.config(state=DISABLED)

    h.config(command=text.xview)
    v.config(command=text.yview)

     
def insertButtons(t:Text, buttons, delete_buttons):
    for i in range(len(buttons)):
        t.insert("1.0", '\n\n')
        t.config(font=('times new rommon', 10))
        t.spacing2 = 20
        t.window_create("1.0", window=buttons[i])
        t.window_create("1.1", window=delete_buttons[i])

#=====================================filter functions====================================
def find_by_number(F2: Frame, ph_no):
    text.forget()
    h.forget()
    v.forget()
    if ph_no!='':
        result = findBillDataByfilter('number' ,ph_no)
        if not result:
            noDataFound(F2)
        else:
            insertBillData(F2, result)

def find_by_bill_no(F2: Frame, bill_no):
    text.forget()
    h.forget()
    v.forget()
    if bill_no != '':
        result = findBillDataByfilter('bill_no', bill_no)
        if not result:
            noDataFound(F2)
        else:
            insertBillData(F2, result)

def find_by_name(F2: Frame, name):
    text.forget()
    h.forget()
    v.forget()
    if name != '':
        result = findBillDataByfilter('name', name)
        if not result:
            noDataFound(F2)
        else:
            insertBillData(F2, result)

def find_by_date(F2: Frame, day, month, year):
    date = year +'-'+ month +'-'+ day
    text.forget()
    h.forget()
    v.forget()
    if day!='' and month != '' and year != '':
        result = findBillDataByfilter('date', date)
        if not result:
            noDataFound(F2)
        else:
            insertBillData(F2, result)

def clear_funciton(F2: Frame):
    text.forget()
    h.forget()
    v.forget()
    result = findBillData()
    if not result:
            noDataFound(F2)
    else:
        insertBillData(F2, result)

#=======================================validation of entry================================

def validate_number(P):
    if len(P) == 0:
        return True
    elif len(P) <= 10 and P.isdigit():
        return True
    else:
        return False

def validate_date_dd_mm(P):
    if len(P) == 0:
        return True
    elif len(P) <= 2 and P.isdigit():
        return True
    else:
        return False


def validate_date_yy(P):
    if len(P) == 0:
        return True
    elif len(P) <= 4 and P.isdigit():
        return True
    else:
        return False
    
def validate_bill_no(P):
    if len(P) == 0:
        return True
    elif P.isdigit():
        return True
    else:
        return False
    

# ==================================================================================================

def findbill_function():
    global text, buttons, h, v
    window = tkinter.Tk()
    window.config(bg=u.find_bill_bg)
    window.title("Find Bill")
    window.geometry('1700x800')

    F1 = LabelFrame(window, bg=u.find_bill_bg)
    F1.place(x=7, y=40, width=1480, height=50)
    top_text = 'Cust_id         Cust_Name                                  Cust_Number                                           Bill_Date        Bill_No        '
    top_layer = Label(F1, text=top_text, font=('timesnew romman', 12), bg='#'+u.blue, fg='white')
    top_layer.grid(column=0, row=1)

    F2 = LabelFrame(window, bg=u.find_bill_bg)
    F2.place(x=7, y=80, width=1480, height=800)



    # =======================================================buttons and labels====================================
    number_vcmd = (window.register(validate_number), '%P')
    dd_mm_vcmd = (window.register(validate_date_dd_mm), '%P')
    yy_vcmd = (window.register(validate_date_yy), '%P')
    bill_no_vcmd = (window.register(validate_bill_no), '%P')

    number_search_label = Label(window, text='Number', font=('times new romman', 10), bg=u.find_bill_bg)
    number_search_label.grid(row=0, column=0, padx=20)
    number_search_entry = Entry(window, validate="key", validatecommand=number_vcmd, width = 20, font='arial 12', highlightthickness=2, highlightcolor='#'+u.green)
    number_search_entry.grid(row=0, column=1)
    number_search_button = Button(window, text='^', font=('times new romman',12), command=lambda:find_by_number(F2, number_search_entry.get()), bg='green')
    number_search_button.grid(row=0, column=2)


    date_search_label = Label(window, text='Date', font=('timesnew romman', 10), bg=u.find_bill_bg)
    date_search_label.grid(row=0, column=3, padx=20)
    date_search_entry = Label(window, text='Date', font=('timesnew romman', 10), bg=u.find_bill_bg)
    date_search_entry.grid(row=0, column=4)
    date_dd = Entry(date_search_entry, validate="key", validatecommand=dd_mm_vcmd, width = 5, font='arial 12', highlightthickness=2, highlightcolor='#'+u.green)
    date_dd.grid(row=0, column=0)
    dd_label = Label(date_search_entry, text='/', font=('timesnew romman', 10), bg=u.find_bill_bg)
    dd_label.grid(row=0, column=1)
    date_mm = Entry(date_search_entry, validate="key", validatecommand=dd_mm_vcmd, width = 5, font='arial 12', highlightthickness=2, highlightcolor='#'+u.green)
    date_mm.grid(row=0, column=2)
    dd_label = Label(date_search_entry, text='/', font=('timesnew romman', 10), bg=u.find_bill_bg)
    dd_label.grid(row=0, column=3)
    date_yy = Entry(date_search_entry, validate="key", validatecommand=yy_vcmd, width = 8, font='arial 12', highlightthickness=2, highlightcolor='#'+u.green)
    date_yy.grid(row=0, column=4)
    date_search_button = Button(window, text='^', font=('times new romman',12), command=lambda:find_by_date(F2, date_dd.get(), date_mm.get(), date_yy.get()), bg='green')
    date_search_button.grid(row=0, column=5)

    bill_no_search_label = Label(window, text='Bill_no', font=('timesnew romman', 10), bg=u.find_bill_bg)
    bill_no_search_label.grid(row=0, column=6, padx=20)
    bill_no_search_entry = Entry(window, validate="key", validatecommand=bill_no_vcmd, width = 20, font='arial 12', highlightthickness=2, highlightcolor='#'+u.green)
    bill_no_search_entry.grid(row=0, column=7)
    bill_no_search_button = Button(window, text='^', font=('times new romman',12), command=lambda:find_by_bill_no(F2, bill_no_search_entry.get()), bg='#'+u.green)
    bill_no_search_button.grid(row=0, column=8)

    name_search_label = Label(window, text='Name', font=('timesnew romman', 10), bg=u.find_bill_bg)
    name_search_label.grid(row=0, column=9, padx=20)
    name_search_entry = Entry(window, width = 20, font='arial 12', highlightthickness=2, highlightcolor='#'+u.green)
    name_search_entry.grid(row=0, column=10)
    name_search_button = Button(window, text='^', font=('times new romman',12), command=lambda:find_by_name(F2, name_search_entry.get()), bg='#'+u.green)
    name_search_button.grid(row=0, column=11)

    clear_btn = Button(window, text='Clear', font=('times new romman',12), command=lambda:clear_funciton(F2), bg='#'+u.red)
    clear_btn.grid(row=0, column=12, padx=100)

    # ===================================================================================================================
    
    result = findBillData()
    if not result:
            messagebox.showerror("NO BILL FOUND", 'No Bills are found')
            window.destroy()
    else:
        insertBillData(F2, result)

    window.mainloop()





# if bill_total!=None:
    #     k = ornament - len(bill_total[0])
    #     ret += bill_total[0]
    #     while k>0:
    #         k = k-1
    #         ret += ' '
    #     ret += '      '
    #     k = total - len(str(bill_total[1]))
    #     ret += str(bill_total[1])
    #     while k>0:
    #         k = k-1
    #         ret += ' '
    # else:
    #     k = ornament
    #     while k>0:
    #         k = k-1
    #         ret += ' '
    #     ret += '      '    
    #     k = total
    #     while k>0:
    #         k = k-1
    #         ret += ' '
        