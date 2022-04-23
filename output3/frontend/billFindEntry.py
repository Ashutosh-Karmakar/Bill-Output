from baseInitialization import UiFields
from tkinter import *


def found(u: UiFields, data):
    for l in range(0, 28):
        for m in range(0, 11):
            # print(data[l][m])
            if str(data[l][m]) == 'nan':
                data[l][m] = ''

    u.mobile_txt.delete(0, END)
    u.mobile_txt.insert(0, data[4][5])

    u.name_txt.delete(0, END)
    u.name_txt.insert(0, data[4][1])

    u.addhar_txt.delete(0, END)
    u.addhar_txt.insert(0, data[4][8])

    u.address_txt.delete(0, END)
    u.address_txt.insert(0, data[4][10])

    u.bill_txt_entry.config(state='normal')
    u.bill_txt_entry.delete(0, END)
    u.bill_txt_entry.insert(0, 1)
    u.bill_txt_entry.config(state=DISABLED)

    for i in range(0, 9):
        u.cgst_txt[i].config(state='normal')
        u.sgst_txt[i].config(state='normal')
        u.gstAmt_txt[i].config(state='normal')
        u.mc_txt[i].config(state='normal')

        u.des_txt[i].delete(0, END)
        u.des_txt[i].insert(0, data[8 + i][1])

        u.wt_txt[i].delete(0, END)
        u.wt_txt[i].insert(0, data[8 + i][5])

        u.mc_txt[i].delete(0, END)
        u.mc_txt[i].insert(0, data[8 + i][6])

        u.unit_txt[i].delete(0, END)
        u.unit_txt[i].insert(0, data[8 + i][7])

        u.cgst_txt[i].delete(0, END)
        u.cgst_txt[i].insert(0, data[8 + i][8])

        u.sgst_txt[i].delete(0, END)
        u.sgst_txt[i].insert(0, data[8 + i][9])

        u.net_txt[i].delete(0, END)
        u.net_txt[i].insert(0, data[8 + i][10])

        u.cgst_txt[i].config(state=DISABLED)
        u.sgst_txt[i].config(state=DISABLED)
        u.gstAmt_txt[i].config(state=DISABLED)
        u.mc_txt[i].config(state=DISABLED)

    for i in range(0, 3):
        u.oldwe_txt[i].delete(0, END)
        u.oldwe_txt[i].insert(0, data[18 + i][8])

        u.oldunit_txt[i].delete(0, END)
        u.oldunit_txt[i].insert(0, data[18 + i][9])

        u.oldtotal_txt[i].delete(0, END)
        u.oldtotal_txt[i].insert(0, data[18 + i][10])

    for i in range(0, 3):
        u.addtotal_txt[i].delete(0, END)
        u.addtotal_txt[i].insert(0, data[23 + i][10])

    # u.mode.center(data[26][8])
    u.total.delete(0, END)
    u.total.insert(0, data[27][10])
