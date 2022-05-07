from tkinter import *

from baseInitialization import UiFields
from common import createCalender, visual_date_convert, date_to_string
from database import findGRDate


def findGoldRateOnDate(u: UiFields):
    root = Tk()
    root.configure(bg=u.background_color)
    root.title("Gold Rate")
    root.geometry("400x600")
    cal = createCalender(root)
    cal.pack(pady=20)

    def grad_date():
        dat = cal.get_date()
        u.cal1 = date_to_string(dat)
        u.grFindDate = visual_date_convert(dat)
        print(u.grFindDate)
        i = findGRDate(u)

        date.config(text="Selected Date is: " + u.grFindDate)
        goldRate.config(text=u.grRateOnDate)
        goldRate.config(font=("times new rommon", 11))

    Button(root, text="Get Date",
           command=grad_date, font=('times new rommon Bold', 11), fg='white', bg='#' + u.green).pack(pady=20)

    date = Label(root, text="", font=('times new rommon Bold', 11),bg=u.bg_color)
    date.pack(pady=20)
    goldRate = Label(root, text="", font=('times new rommon Bold', 11),bg=u.bg_color)
    goldRate.pack(pady=20)

    root.mainloop()
