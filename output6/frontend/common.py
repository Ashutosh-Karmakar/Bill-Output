from datetime import datetime
from tkcalendar import Calendar
from tkinter import *


def createCalender(root):
    cur_date = datetime.now()
    cal = Calendar(root, selectmode='day',
                   year=cur_date.year, month=cur_date.month,
                   day=cur_date.day)
    return cal


def date_to_string(date):
    if type(date) == str:
        return datetime.strptime(date, '%m/%d/%y')
    if type(date) == datetime:
        return date.strftime('%d-%m-%Y')


def visual_date_convert(date):
    datefind = ''
    result = date
    result = result.split('/')

    datefind = datefind + '20' + result[2] + '-'
    if len(result[0]) == 1:
        result[0] = '0' + result[0]
    datefind = datefind + result[0] + '-'

    if len(result[1]) == 1:
        result[1] = '0' + result[1]
    datefind = datefind + result[1]
    return datefind


def insert_into_disabled(widget, value):
    widget.config(state='normal')
    widget.delete(0, END)
    widget.insert(0, value)
    widget.config(state=DISABLED)

def insert_after_delete(widget, value):
    widget.delete(0, END)
    widget.insert(0, value)


def clicked_tab(focused_top):
    if focused_top == '.!entry':
        return 0
    if focused_top == '.!entry2':
        return 1
    if focused_top == '.!entry3':
        return 2
    if focused_top == '.!entry4':
        return 3
    if focused_top == '.!labelframe.!entry':
        return 4
    if focused_top == '.!labelframe.!entry2':
        return 5
    if focused_top == '.!labelframe.!entry3':
        return 6
    if focused_top == '.!labelframe.!entry9':
        return 7
    if focused_top == '.!labelframe.!entry10':
        return 8
    if focused_top == '.!labelframe.!entry11':
        return 9
    if focused_top == '.!labelframe.!entry17':
        return 10
    if focused_top == '.!labelframe.!entry18':
        return 11
    if focused_top == '.!labelframe.!entry19':
        return 12
    if focused_top == '.!labelframe.!entry25':
        return 13
    if focused_top == '.!labelframe.!entry26':
        return 14
    if focused_top == '.!labelframe.!entry27':
        return 15
    if focused_top == '.!labelframe.!entry33':
        return 16
    if focused_top == '.!labelframe.!entry34':
        return 17
    if focused_top == '.!labelframe.!entry35':
        return 18
    if focused_top == '.!labelframe.!entry41':
        return 19
    if focused_top == '.!labelframe.!entry42':
        return 20
    if focused_top == '.!labelframe.!entry43':
        return 21
    if focused_top == '.!labelframe.!entry49':
        return 22
    if focused_top == '.!labelframe.!entry50':
        return 23
    if focused_top == '.!labelframe.!entry51':
        return 24
    if focused_top == '.!labelframe.!entry57':
        return 25
    if focused_top == '.!labelframe.!entry58':
        return 26
    if focused_top == '.!labelframe.!entry59':
        return 27
    if focused_top == '.!labelframe.!entry65':
        return 28
    if focused_top == '.!labelframe.!entry66':
        return 29
    if focused_top == '.!labelframe.!entry67':
        return 30
    if focused_top == '.!labelframe2.!entry2':
        return 31
    if focused_top == '.!labelframe2.!entry4':
        return 32
    if focused_top == '.!labelframe2.!entry6':
        return 33
    if focused_top == '.!labelframe2.!entry8':
        return 34
    if focused_top == '.!labelframe2.!entry10':
        return 35
    if focused_top == '.!labelframe2.!entry12':
        return 36
    if focused_top == '.!labelframe3.!entry2':
        return 37
    if focused_top == '.!labelframe3.!entry4':
        return 38
    if focused_top == '.!labelframe3.!entry6':
        return 39
    if focused_top == '.!labelframe4.!entry':
        return 40
    if focused_top == '.!labelframe4.!entry2':
        return 41

def focusedTab(focused_tab):
    if focused_tab == '.!entry4':
        return 'addhar'
    if focused_tab == '.!entry':
        return 'number'
    if focused_tab == '.!entry2':
        return 'name'
    if focused_tab == '.!labelframe.!entry' or focused_tab == '.!labelframe.!entry9' or \
            focused_tab == '.!labelframe.!entry17' or focused_tab == '.!labelframe.!entry25' or \
            focused_tab == '.!labelframe.!entry33' or focused_tab == '.!labelframe.!entry41' or \
            focused_tab == '.!labelframe.!entry49' or focused_tab == '.!labelframe.!entry57' or \
            focused_tab == '.!labelframe.!entry65':
        return 'desc'
    if focused_tab == '.!labelframe.!entry2' or focused_tab == '.!labelframe.!entry10' or \
            focused_tab == '.!labelframe.!entry18' or focused_tab == '.!labelframe.!entry26' or \
            focused_tab == '.!labelframe.!entry34' or focused_tab == '.!labelframe.!entry42' or \
            focused_tab == '.!labelframe.!entry50' or focused_tab == '.!labelframe.!entry58' or \
            focused_tab == '.!labelframe.!entry66':
        return 'wt'
    if focused_tab == '.!labelframe.!entry3' or focused_tab == '.!labelframe.!entry11' or \
            focused_tab == '.!labelframe.!entry19' or focused_tab == '.!labelframe.!entry27' or \
            focused_tab == '.!labelframe.!entry35' or focused_tab == '.!labelframe.!entry43' or \
            focused_tab == '.!labelframe.!entry51' or focused_tab == '.!labelframe.!entry59' or \
            focused_tab == '.!labelframe.!entry67':
        return 'newTotal'
    if focused_tab == '.!labelframe2.!entry2' or focused_tab == '.!labelframe2.!entry6' or \
            focused_tab == '.!labelframe2.!entry10':
        return 'oldWt'
    if focused_tab == '.!labelframe2.!entry' or focused_tab == '.!labelframe2.!entry5' or \
            focused_tab == '.!labelframe2.!entry9':
        return 'oldDesc'
    if focused_tab == '.!labelframe3.!entry' or focused_tab == '.!labelframe3.!entry3' or \
            focused_tab == '.!labelframe3.!entry5':
        return 'addDesc'
    if focused_tab == '.!labelframe2.!entry4' or focused_tab == '.!labelframe2.!entry8' or \
            focused_tab == '.!labelframe2.!entry12':
        return 'oldAmt'
    if focused_tab == '.!labelframe3.!entry2' or focused_tab == '.!labelframe3.!entry4' or \
            focused_tab == '.!labelframe3.!entry6':
        return 'addAmt'
    if focused_tab == '.!labelframe4.!entry2':
        return 'charges'
    if focused_tab == '.!labelframe4.!entry3':
        return 'total'

def tabNumber(focused_tab):
    # desc entry:
    if focused_tab == '.!labelframe.!entry':
        return 0
    if focused_tab == '.!labelframe.!entry9':
        return 1
    if focused_tab == '.!labelframe.!entry17':
        return 2
    if focused_tab == '.!labelframe.!entry25':
        return 3
    if focused_tab == '.!labelframe.!entry33':
        return 4
    if focused_tab == '.!labelframe.!entry41':
        return 5
    if focused_tab == '.!labelframe.!entry49':
        return 6
    if focused_tab == '.!labelframe.!entry57':
        return 7
    if focused_tab == '.!labelframe.!entry65':
        return 8

    # wt entry
    if focused_tab == '.!labelframe.!entry2':
        return 0
    if focused_tab == '.!labelframe.!entry10':
        return 1
    if focused_tab == '.!labelframe.!entry18':
        return 2
    if focused_tab == '.!labelframe.!entry26':
        return 3
    if focused_tab == '.!labelframe.!entry34':
        return 4
    if focused_tab == '.!labelframe.!entry42':
        return 5
    if focused_tab == '.!labelframe.!entry50':
        return 6
    if focused_tab == '.!labelframe.!entry58':
        return 7
    if focused_tab == '.!labelframe.!entry66':
        return 8

    # new total
    if focused_tab == '.!labelframe.!entry3':
        return 0
    if focused_tab == '.!labelframe.!entry11':
        return 1
    if focused_tab == '.!labelframe.!entry19':
        return 2
    if focused_tab == '.!labelframe.!entry27':
        return 3
    if focused_tab == '.!labelframe.!entry35':
        return 4
    if focused_tab == '.!labelframe.!entry43':
        return 5
    if focused_tab == '.!labelframe.!entry51':
        return 6
    if focused_tab == '.!labelframe.!entry59':
        return 7
    if focused_tab == '.!labelframe.!entry67':
        return 8

    # old gold desc entry:
    if focused_tab == '.!labelframe2.!entry':
        return 0
    if focused_tab == '.!labelframe2.!entry5':
        return 1
    if focused_tab == '.!labelframe2.!entry9':
        return 2

    # old gold weight
    if focused_tab == '.!labelframe2.!entry2':
        return 0
    if focused_tab == '.!labelframe2.!entry6':
        return 1
    if focused_tab == '.!labelframe2.!entry10':
        return 2

    # old gold amt
    if focused_tab == '.!labelframe2.!entry4':
        return 0
    if focused_tab == '.!labelframe2.!entry8':
        return 1
    if focused_tab == '.!labelframe2.!entry12':
        return 2

    # add desc :
    if focused_tab == '.!labelframe3.!entry':
        return 0
    if focused_tab == '.!labelframe3.!entry3':
        return 1
    if focused_tab == '.!labelframe3.!entry5':
        return 2

    # add amt :
    if focused_tab == '.!labelframe3.!entry2':
        return 0
    if focused_tab == '.!labelframe3.!entry4':
        return 1
    if focused_tab == '.!labelframe3.!entry6':
        return 2


EMPTY = ''
X = [EMPTY, 'One ', 'Two ', 'Three ', 'Four ', 'Five ', 'Six ', 'Seven ', 'Eight ', 'Nine ', 'Ten ', 'Eleven ',
     'Twelve ', 'Thirteen ', 'Fourteen ', 'Fifteen ', 'Sixteen ', 'Seventeen ', 'Eighteen ', 'Nineteen ']
Y = [EMPTY, EMPTY, 'Twenty ', 'Thirty ', 'Forty ', 'Fifty ', 'Sixty ', 'Seventy ', 'Eighty ', 'Ninety ']


def convertToDigit(n, suffix):
    # if `n` is zero
    if n == 0:
        return EMPTY
    # split `n` if it is more than 19
    if n > 19:
        return Y[n // 10] + X[n % 10] + suffix
    else:
        return X[n] + suffix


def convert(n):
    # add digits at ten million and hundred million place
    result = convertToDigit((n // 1000000000) % 100, 'Billion, ')
    # add digits at ten million and hundred million place
    result += convertToDigit((n // 10000000) % 100, 'Crore, ')
    # add digits at hundred thousand and one million place
    result += convertToDigit(((n // 100000) % 100), 'Lakh, ')
    # add digits at thousand and tens thousand place
    result += convertToDigit(((n // 1000) % 100), 'Thousand, ')
    # add digit at hundred place
    result += convertToDigit(((n // 100) % 10), 'Hundred ')
    if n > 100 and n % 100:
        result += 'and '
    # add digits at ones and tens place
    result += convertToDigit((n % 100), '')
    return result.strip().rstrip(',').replace(', and', ' and')
