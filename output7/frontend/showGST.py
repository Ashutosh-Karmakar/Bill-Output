from tkinter import *
import tkinter as tk

from common import date_to_string
from database import findGstData, findGst
from baseInitialization import UiFields


def stringFormation(result):
    if len(result) == 0:
        return None
    gst = []
    for i in result:
        gst_data = ''
        for j in i:
            gst_data += str(j) + '         '
        gst.append(gst_data)


def toggle(u: UiFields, widget):
    values = widget['text'].split('         ')
    id = int(values[0])
    tv = float(str(values[6]))
    ct = float(str(values[7]))
    st = float(str(values[8]))
    nt = float(str(values[9]))

    if widget['bg'] == 'white':
        widget.configure(bg='red')
        u.gst_remove_ids.append(id)
        u.total_val_gst -= tv
        u.cgst_gst -= ct
        u.sgst_gst -= st
        u.net_total_gst -= nt
    else:
        widget.configure(bg='white')
        u.gst_remove_ids.remove(id)
        u.total_val_gst += tv
        u.cgst_gst += ct
        u.sgst_gst += st
        u.net_total_gst += nt

    u.total_val_label_gst.config(text='  Total_amt: ' + str(round(u.total_val_gst, 3)))
    u.cgst_label_gst.config(text='  CGST: ' + str(round(u.cgst_gst, 3)))
    u.sgst_label_gst.config(text='  SGST: ' + str(round(u.sgst_gst, 3)))
    u.net_total_label_gst.config(text='  net_total: ' + str(round(u.net_total_gst, 3)))


def clearIds(u: UiFields):
    u.gst_remove_ids = []


def GoBtn(u: UiFields, root):
    findGst(u)
    # u.gstSend.grid(column=2, row=)
    clearIds(u)
    root.destroy()


def findGSTDisplay(u: UiFields):
    root = Tk()
    topleveldetail = Label(root, text='    si        Date         Description    Qty     Weight       UnitPrice        TotalAmt        Cgst        Sgst        NetTotal ', borderwidth=2, relief="solid", font=('times new rommon', 13))
    topleveldetail.pack(side=tk.TOP, anchor=NW)

    h = Scrollbar(root, orient='horizontal')
    h.pack(side=BOTTOM, fill=X)
    v = Scrollbar(root, orient='vertical')
    v.pack(side=RIGHT, fill=Y)

    text = Text(root, width=130, height=30, wrap=NONE,
             xscrollcommand=h.set,
             yscrollcommand=v.set)
    result, sum_result = findGstData(u)

    for i in range(len(result)):
        cb = tk.Checkbutton(text, text=result[i], bg='white', anchor='w')
        cb.configure(command=lambda widget=cb: toggle(u, widget))
        text.window_create('end', window=cb)
        text.insert('end', '\n')
    #
    text.pack(side=TOP, fill=X)

    h.config(command=text.xview)
    v.config(command=text.yview)

    u.total_val_gst = float(round(sum_result[0][0], 3))
    u.total_val_label_gst = Label(root, text='  Total_amt: ' + str(u.total_val_gst) + '  ', borderwidth=2, relief="solid", font=('times new rommon', 13))
    u.total_val_label_gst.pack(side=tk.LEFT, padx=10,pady=10)

    u.cgst_gst = float(round(sum_result[0][1], 3))
    u.cgst_label_gst = Label(root, text='  CGST: ' + str(u.cgst_gst) + '  ', borderwidth=2, relief="solid", font=('times new rommon', 13))
    u.cgst_label_gst.pack(side=tk.LEFT, padx=10,pady=10)

    Go = Button(root, text="Go", font=('times new rommon', 13), command=lambda: GoBtn(u, root), bg='#'+u.red)
    Go.pack(side=tk.LEFT)

    u.sgst_gst = float(round(sum_result[0][2], 3))
    u.sgst_label_gst = Label(root, text='  SGST: ' + str(u.sgst_gst) + '  ', borderwidth=2, relief="solid", font=('times new rommon', 13))
    u.sgst_label_gst.pack(side=tk.LEFT, padx=10,pady=10)

    u.net_total_gst = float(round(sum_result[0][3], 3))
    u.net_total_label_gst = Label(root, text='  net_total: ' + str(u.net_total_gst) + '  ', borderwidth=2, relief="solid", font=('times new rommon', 13))
    u.net_total_label_gst.pack(side=tk.RIGHT, padx=10,pady=10)

    root.mainloop()



# findGSTDisplay()