from tkinter import *
from tkinter import messagebox

from baseInitialization import UiFields
from common import insert_into_disabled, insert_after_delete, focusedTab, tabNumber
from database import findBillNumber, findByNumber


def check_clicked_tab(u: UiFields):
    if u.entryCount == 0:
        u.mobile_txt.configure(highlightcolor=u.entry_wrong_color)
        u.mobile_txt.focus()
        return 1
    if u.entryCount == 1:
        u.name_txt.configure(highlightcolor=u.entry_wrong_color)
        u.name_txt.focus()
        return 1
    if u.entryCount == 6 or u.entryCount == 9 or u.entryCount == 12 or u.entryCount == 15 or u.entryCount == 18 or\
            u.entryCount == 21 or u.entryCount == 24 or u.entryCount == 27 or u.entryCount == 30:
        u.entry_list[u.entryCount].configure(highlightcolor=u.entry_wrong_color)
        u.entry_list[u.entryCount].focus()
        return 1
    if u.entryCount == 32 or u.entryCount == 34 or u.entryCount == 36:
        u.entry_list[u.entryCount].configure(highlightcolor=u.entry_wrong_color)
        u.entry_list[u.entryCount].focus()
        return 1
    if u.entryCount == 37 or u.entryCount == 38 or u.entryCount == 39:
        u.entry_list[u.entryCount].configure(highlightcolor=u.entry_wrong_color)
        u.entry_list[u.entryCount].focus()
        return 1


def setCustData(u: UiFields, data):
    print('cust Data', data)
    insert_after_delete(u.name_txt, data[1])
    insert_after_delete(u.address_txt, data[3])
    if data[4] is None:
        insert_after_delete(u.addhar_txt, '')
    else:
        insert_after_delete(u.addhar_txt, data[4])
    u.addhar_txt.focus_set()
    u.entryCount = 4


def calculate(u: UiFields, i, by='backend'):
    try:
        print(i)
        wt = float(u.wt_txt[i].get())
        amt = float(u.net_txt[i].get())
        gr = u.gold_rate
        cost = amt * (100 / 103)
        u.total_taxable_amt.append(cost)
        if cost < amt:
            cgst = amt - cost
        else:
            cgst = 0
        print('cost - ', cost)
        print('wt - ', wt)

        mc = (cost / wt) - gr
        mc = round(mc, 2)
        cgst = round(cgst / 2, 2)
        gstamt = cgst * 2

        if mc < 0:
            if by == 'backend':
                print("There is a error in calculation mc")
                u.entryCount = 6 + i * 3
                u.wt_txt[i].focus()
                u.net_txt[i].configure(highlightcolor=u.entry_wrong_color)
                # u.total_before_charge = u.total_before_charge - float(u.net_txt[i].get())
                return 1
            else:
                startOverGOLDRATE(u)
                print("There is a error in calculation mc")
                messagebox.showerror("Error", 'GOLD RATE IS TOO HIGH')
                return 1

        insert_into_disabled(u.cgst_txt[i], cgst)
        insert_into_disabled(u.sgst_txt[i], cgst)
        insert_into_disabled(u.gstAmt_txt[i], gstamt)
        insert_into_disabled(u.mc_txt[i], mc)

        u.gstAmt_txt[i].focus_set()
    except Exception as e:
        print("there is a error in calculation")
        # u.des_txt[i].focus_set()
        messagebox.showerror("Error", "There is a error in calculation: {0}".format(e))


def set_total_after_charges(u: UiFields):
    try:
        if u.total.get() != '' and u.charge.get() != '':
            tot = float(u.total_before_charge)
            cha = float(u.charge_amt)
            tot = round(tot + tot * (cha / 100), 2)
            insert_after_delete(u.total, tot)
        elif u.total.get() != '':
            tot = float(u.total_before_charge)
            cha = float(u.charge_amt)
            tot = round(tot - tot * (cha / 100), 2)
            # u.total.delete(0, END)
            # u.total.insert(0, round(u.total_before_charge, 2))
            insert_after_delete(u.total, round(u.total_before_charge, 2))
            u.charge_amt = 0.0
    except Exception as e:
        print("There is a exception : {0}".format(e))


def findAmt(amt):
    try:
        return float(amt.get())
    except Exception as e:
        print("There is a exception : {0}".format(e))
        return 0


def setTotal(u: UiFields, amt):
    try:
        if u.charge.get() != '':
            amt = round(amt + (amt * (float(u.charge_amt) / 100)), 2)
        insert_after_delete(u.total, amt)
    except Exception as e:
        print("There is a exception : {0}".format(e))


def checkField(focused_tab, u: UiFields):
    tab_name = focusedTab(focused_tab)
    i = tabNumber(focused_tab)

    # name
    if tab_name == 'name':
        if u.name_txt.get() == '':
            return True
        return False

    # number
    if tab_name == 'number':
        if u.mobile_txt.get() == '':
            return True
        if len(u.mobile_txt.get()) != 10:
            return True
        for ch in u.mobile_txt.get():
            if ch == '.':
                return True
            elif not ch.isnumeric():
                return True
        return False

    # wt field and net total:
    if tab_name == 'wt':
        if u.wt_txt[i].get() != '' and (u.wt_txt[i].get()).isalpha():
            return True
        if len(u.wt_txt[i].get()) == 1 and (ord(str(u.wt_txt[i].get())) < 48 or ord(str(u.wt_txt[i].get())) > 57):
            return True
        if len(u.wt_txt[i].get()) > 1:
            ct = 0
            for ch in u.wt_txt[i].get():
                if ch == '.':
                    ct += 1
                elif ch != '.' and ch.isnumeric() is False:
                    return True
                if ct >= 2:
                    return True
        return False

    elif tab_name == 'newTotal':
        if u.net_txt[i].get() != '' and (u.net_txt[i].get()).isalpha():
            return True
        if len(u.net_txt[i].get()) == 1 and (ord(str(u.net_txt[i].get())) < 48 or ord(str(u.net_txt[i].get())) > 57):
            return True
        if len(u.net_txt[i].get()) > 1:
            ct = 0
            for ch in u.net_txt[i].get():
                if ct >= 2:
                    return True
                elif ch == '.':
                    ct += 1
                elif ch != '.' and ch.isnumeric() is False:
                    return True
        return False

    elif tab_name == 'oldWt':
        if u.oldwe_txt[i].get() != '' and (u.oldwe_txt[i].get()).isalpha():
            return True
        if len(u.oldwe_txt[i].get()) == 1 and (
                ord(str(u.oldwe_txt[i].get())) < 48 or ord(str(u.oldwe_txt[i].get())) > 57):
            return True
        if len(u.oldwe_txt[i].get()) > 1:
            ct = 0
            for ch in u.oldwe_txt[i].get():
                if ct >= 2:
                    return True
                elif ch == '.':
                    ct += 1
                elif ch != '.' and ch.isnumeric() is False:
                    return True
        return False

    elif tab_name == 'oldAmt':
        if u.oldtotal_txt[i].get() != '' and (u.oldtotal_txt[i].get()).isalpha():
            return True
        if len(u.oldtotal_txt[i].get()) == 1 and (
                ord(str(u.oldtotal_txt[i].get())) < 48 or ord(str(u.oldtotal_txt[i].get())) > 57):
            return True
        if len(u.oldtotal_txt[i].get()) > 1:
            ct = 0
            for ch in u.oldtotal_txt[i].get():
                if ct >= 2:
                    return True
                elif ch == '.':
                    ct += 1
                elif ch != '.' and ch.isnumeric() is False:
                    return True
        return False

    elif tab_name == 'addAmt':
        if u.addtotal_txt[i].get() != '' and (u.addtotal_txt[i].get()).isalpha():
            return True
        if len(u.addtotal_txt[i].get()) == 1 and (
                ord(str(u.addtotal_txt[i].get())) < 48 or ord(str(u.addtotal_txt[i].get())) > 57):
            return True
        if len(u.addtotal_txt[i].get()) > 1:
            ct = 0
            for ch in u.addtotal_txt[i].get():
                if ct >= 2:
                    return True
                elif ch == '.':
                    ct += 1
                elif ch != '.' and ch.isnumeric() is False:
                    return True
        return False

    elif tab_name == 'addhar':
        if u.addhar_txt.get() != '' and (u.addhar_txt.get()).isnumeric() is False:
            return True


def enterOperation(focused_tab, u: UiFields):
    tab_name = focusedTab(focused_tab)
    i = tabNumber(focused_tab)
    print(focused_tab)

    if checkField(focused_tab, u):
        if tab_name == 'name':
            u.mobile_txt.focus_set()
            u.name_txt.configure(highlightcolor=u.entry_wrong_color)
            return
        elif tab_name == 'number':
            u.mobile_txt.focus_set()
            u.mobile_txt.configure(highlightcolor=u.entry_wrong_color)
            return 1
        elif tab_name == 'wt':
            u.des_txt[i].focus_set()
            u.wt_txt[i].configure(highlightcolor=u.entry_wrong_color)
            return

        elif tab_name == 'newTotal':
            u.wt_txt[i].focus_set()
            u.net_txt[i].configure(highlightcolor=u.entry_wrong_color)
            return

        elif tab_name == 'oldWt':
            u.oldDesc_txt[i].focus_set()
            u.oldwe_txt[i].configure(highlightcolor=u.entry_wrong_color)
            return

        elif tab_name == 'oldAmt':
            u.oldwe_txt[i].focus_set()
            u.oldtotal_txt[i].configure(highlightcolor=u.entry_wrong_color)
            return

        elif tab_name == 'addAmt':
            u.addDesc_txt[i].focus_set()
            u.addtotal_txt[i].configure(highlightcolor=u.entry_wrong_color)
            return

        elif tab_name == 'addhar':
            u.address_txt.focus_set()
            u.addhar_txt.configure(highlightcolor=u.entry_wrong_color)
            return

    u.entry_list[u.entryCount].configure(highlightcolor=u.entry_correct_color)
    if u.entryCount >= 42:
        u.entryCount = 42
        print("hello")
        u.entry_list[u.entryCount].focus()

    else:
        u.entryCount += 1

    print('Entry Count :-', u.entryCount)

    if tab_name == 'name' and u.name_txt.get() != '':
        name = u.name_txt.get()
        insert_after_delete(u.name_txt, name.capitalize())

    if tab_name == 'desc' and u.des_txt[i].get() != '':
        des = u.des_txt[i].get()
        insert_after_delete(u.des_txt[i], des.capitalize())

    if u.cnt > 0:
        u.cnt = 0
        if u.old_tab_name == 'desc' and u.des_txt[i].get() == '':
            u.oldDesc_txt[0].focus_set()
            u.entryCount = 31

        if u.old_tab_name == 'oldAmt':
            u.oldtotal_txt[2].focus_set()
            u.entryCount = 38

    if (tab_name == 'desc' and u.des_txt[i].get() == '') \
            or (tab_name == 'oldAmt' and u.oldtotal_txt[i].get() == '') \
            or (tab_name == 'addAmt' and u.addtotal_txt[i].get() == ''):
        u.cnt = u.cnt + 1
        u.old_tab_name = tab_name

    if tab_name == 'number' and u.mobile_txt.get() != '':
        data = findByNumber(u.mobile_txt.get())
        if data != 0:
            setCustData(u, data)

    elif tab_name == 'newTotal' and (u.des_txt[i].get() != '' and u.wt_txt[i].get() != '' and u.net_txt[i].get() != ''):
        try:
            i = tabNumber(focused_tab)
            chec = calculate(u, i, 'backend')
            if chec == 1:
                return
            total = float(u.total_before_charge)
            amt = float(u.net_txt[i].get())
            u.total_before_charge = amt + total
            if u.old_net_total[i] == amt:
                u.total_before_charge = total
                return
            elif u.old_net_total[i] != 0:
                u.total_before_charge = u.total_before_charge - u.old_net_total[i]

            setTotal(u, round(u.total_before_charge, 2))
            u.old_net_total[i] = amt
        except Exception as e:
            print("There is a exception : {0}".format(e))

    elif tab_name == 'oldAmt' and u.oldtotal_txt[i].get() != '' and checkField(focused_tab, u) is False:
        total = u.total_before_charge
        amt = findAmt(u.oldtotal_txt[i])
        u.total_before_charge = total - amt
        if u.old_old_total[i] == amt:
            u.total_before_charge = total
            return
        elif u.old_old_total[i] != 0:
            u.total_before_charge = u.total_before_charge + u.old_old_total[i]

        setTotal(u, round(u.total_before_charge, 2))
        u.old_old_total[i] = amt

    elif tab_name == 'addAmt' and u.addtotal_txt[i].get() != '' and checkField(focused_tab, u) is False:
        total = u.total_before_charge
        amt = findAmt(u.addtotal_txt[i])
        u.total_before_charge = total + amt
        if u.old_add_total[i] == amt:
            u.total_before_charge = total
            return
        elif u.old_add_total[i] != 0:
            print(u.old_add_total[i])
            u.total_before_charge = u.total_before_charge - u.old_add_total[i]
        setTotal(u, round(u.total_before_charge, 2))
        u.old_add_total[i] = amt


def newBill(u: UiFields):
    u.mobile_txt.delete(0, END)
    u.mobile_txt.configure(highlightcolor=u.entry_correct_color)
    u.name_txt.delete(0, END)
    u.name_txt.configure(highlightcolor=u.entry_correct_color)
    u.address_txt.delete(0, END)
    u.address_txt.configure(highlightcolor=u.entry_correct_color)
    u.addhar_txt.delete(0, END)
    u.addhar_txt.configure(highlightcolor=u.entry_correct_color)
    u.bill_txt = findBillNumber()
    insert_into_disabled(u.bill_txt_entry, u.bill_txt)
    u.mobile_txt.focus()
    u.entryCount = 0
    cleanStart(u)


def startOverGOLDRATE(u: UiFields):
    u.des_txt[0].focus()
    u.entryCount = 4
    cleanStart(u)


def cleanStart(u: UiFields):
    u.bill_generated = False
    u.charge_amt = 0.0
    u.total_before_charge = 0.0
    u.old_net_total = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    u.old_old_total = [0, 0, 0]
    u.old_add_total = [0, 0, 0]
    u.total_taxable_amt = []
    # ========================================new Gold==============================================
    for i in range(0, 9):
        if u.des_txt[i].get() != '':
            u.des_txt[i].delete(0, END)
            u.des_txt[i].configure(highlightcolor=u.entry_correct_color)

            u.wt_txt[i].delete(0, END)
            u.wt_txt[i].configure(highlightcolor=u.entry_correct_color)

            u.net_txt[i].delete(0, END)
            u.net_txt[i].configure(highlightcolor=u.entry_correct_color)

            u.mc_txt[i].config(state='normal')
            u.mc_txt[i].delete(0, END)
            u.mc_txt[i].configure(highlightcolor=u.entry_correct_color)
            u.mc_txt[i].config(state=DISABLED)

            u.cgst_txt[i].config(state='normal')
            u.cgst_txt[i].delete(0, END)
            u.cgst_txt[i].configure(highlightcolor=u.entry_correct_color)
            u.cgst_txt[i].config(state=DISABLED)

            u.sgst_txt[i].config(state='normal')
            u.sgst_txt[i].delete(0, END)
            u.sgst_txt[i].configure(highlightcolor=u.entry_correct_color)
            u.sgst_txt[i].config(state=DISABLED)

            u.gstAmt_txt[i].config(state='normal')
            u.gstAmt_txt[i].delete(0, END)
            u.gstAmt_txt[i].configure(highlightcolor=u.entry_correct_color)
            u.gstAmt_txt[i].config(state=DISABLED)

    # ==================================old gold=====================================================

    for i in range(0, 3):
        u.oldDesc_txt[i].configure(highlightcolor=u.entry_correct_color)
        insert_after_delete(u.oldDesc_txt[i], 'Old Gold')

        u.oldwe_txt[i].delete(0, END)
        u.oldwe_txt[i].configure(highlightcolor=u.entry_correct_color)

        u.oldtotal_txt[i].delete(0, END)
        u.oldtotal_txt[i].configure(highlightcolor=u.entry_correct_color)

    # ===========================================addition or deduction===============================

    for i in range(0, 3):
        u.addDesc_txt[i].delete(0, END)
        u.addDesc_txt[i].configure(highlightcolor=u.entry_correct_color)

        u.addtotal_txt[i].delete(0, END)
        u.addtotal_txt[i].configure(highlightcolor=u.entry_correct_color)

    # =================================mode of payment and total==============================

    u.clicked.set('Cash')
    u.charge.delete(0, END)

    u.total.configure(highlightcolor=u.entry_correct_color)
    insert_after_delete(u.total, 0)
