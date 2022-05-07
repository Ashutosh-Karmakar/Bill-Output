import tkinter
from tkinter import *

from baseInitialization import UiFields
from common import createCalender, date_to_string, visual_date_convert
from database import findGst, findConfigValue
from gstexel import send_email


def monthlyGst(u: UiFields):
    u.email_from_address = findConfigValue('email_sender_address')
    u.email_to_address = findConfigValue('email_receiver_address')
    u.email_from_pass = findConfigValue('email_from_pass')
    u.BASEDIR_GST = findConfigValue('BASEDIR_GST')

    window = tkinter.Tk()
    window.geometry('1000x800')
    window.configure(bg=u.background_color)
    window.title("Monthly GST")

    llFrom = Label(window, text="FROM", font=('times new rommon', 14), bg=u.bg_color).grid(row=0, column=0)
    u.gstDateFrom_label = Label(window, text='Billing Date:', font=('times new rommon', 11), bg=u.bg_color)
    u.gstDateFrom_label.grid(row=1, column=0)

    calfrom = createCalender(window)

    calfrom.grid(row=2, column=0)

    u.gstDateFrom = Label(window, text="", font=('times new rommon', 11), bg=u.bg_color)
    u.gstDateFrom.grid(row=1, column=1)

    llFrom = Label(window, text="TO", font=('times new rommon', 14), bg=u.bg_color).grid(row=0, column=3)
    u.gstDateTo_label = Label(window, text='Billing Date:', font=('times new rommon', 11), bg=u.bg_color)
    u.gstDateTo_label.grid(row=1, column=3)

    calto = createCalender(window)

    calto.grid(row=2, column=3)

    u.gstDateTo = Label(window, text="", font=('times new rommon', 11), bg=u.bg_color)
    u.gstDateTo.grid(row=1, column=4)

    u.gstFind = Button(window, text="Find", font=('times new rommon', 13), command=lambda: findGst(u), fg='white', bg='#' + u.blue, bd=2)
    u.gstFind.grid(column=1, row=4)
    u.gstFind.grid_forget()

    u.gstSend = Button(window, text="Send", font=('times new rommon', 13), command=lambda: send_email(u), fg='white', bg='#' + u.red, bd=2)
    u.gstSend.grid(column=2, row=4)
    u.gstSend.grid_forget()

    llmsg = Label(window, text="FROM should be less than TO", font=('times new rommon', 11), bg=u.bg_color)
    llmsg.grid(column=1, row=4)

    def grad_date(cal, n):
        datefind = visual_date_convert(cal.get_date())
        if n == 1:
            u.gstDateFrom.config(text=datefind)
            u.cal1 = date_to_string(cal.get_date())
            print(u.cal1)
        if n == 2:
            u.gstDateTo.config(text=datefind)
            u.cal2 = date_to_string(cal.get_date())
            print(u.cal2)

        if u.gstDateFrom["text"] != "" and u.gstDateTo["text"] != "":
            if u.cal1 <= u.cal2:
                llmsg.grid_forget()
                u.gstFind.grid(column=1, row=4)
            else:
                u.gstFind.grid_forget()
                llmsg.grid(column=1, row=4)

    Button(window, text="Get Date",
           command=lambda: grad_date(calfrom, 1), font=('times new rommon Bold', 11), fg='white', bg='#' + u.green).grid(row=3, column=0)
    Button(window, text="Get Date",
           command=lambda: grad_date(calto, 2), font=('times new rommon Bold', 11), fg='white', bg='#' + u.green).grid(row=3, column=3)

    window.mainloop()
