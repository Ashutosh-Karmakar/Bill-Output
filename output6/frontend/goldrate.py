import tkinter as tk
from tkinter import simpledialog
from tkinter import messagebox

from backend import calculate
from baseInitialization import UiFields
from common import insert_into_disabled
from database import saveGoldRate


def changeGoldRate(u: UiFields):
    gr = tk.Tk()
    gr.withdraw()
    gold_rate = simpledialog.askstring(title="Gold Rate", prompt="Gold Rate?:")
    if gold_rate is None:
        return
    if not gold_rate.isnumeric():
        messagebox.showerror("Error", "Gold Rate can only be number")
        return
    if len(gold_rate) > 4:
        tens = 10 ** (len(gold_rate) - 4)
        u.gold_rate = int(gold_rate) // tens
    else:
        u.gold_rate = int(gold_rate)
    saveGoldRate(u)
    for i in range(0, 9):
        insert_into_disabled(u.unit_txt[i], u.gold_rate)

    u.old_gold_rate = u.gold_rate - 100

    for i in range(0, 3):
        insert_into_disabled(u.oldunit_txt[i], u.old_gold_rate)

    if u.mobile_txt.get() == '':
        u.mobile_txt.focus()
        u.entryCount = 0
        return
    l = 0
    for l in range(0, 10):
        if u.des_txt[l].get() == '':
            u.des_txt[l].focus()
            u.entryCount = 4 + l * 3
            break
        if u.wt_txt[l].get() == '':
            u.wt_txt[l].focus()
            u.entryCount = 5 + l * 3
            break
        if u.net_txt[l].get() == '':
            u.net_txt[l].focus()
            u.entryCount = 6 + l * 3
            break
        mm = calculate(u, l, 'goldrate')
        if mm == 1:
            break
    if l == 10:
        u.oldwe_txt[0].focus()
