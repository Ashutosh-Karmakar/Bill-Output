import mysql.connector
import sys
from tkinter import messagebox

from baseInitialization import UiFields
from gstexel import create, insertTotal

try:
    mysqlDB = mysql.connector.connect(
        host='localhost',
        user='root',
        passwd='1234',
        database='Shop',
        auth_plugin='mysql_native_password'
    )
    cursor = mysqlDB.cursor()
except Exception as e:
    messagebox.showerror("Error", "Error in CONNECTING TO DATABASE : {0}".format(e))
    sys.exit()


def saveCustomerData(u: UiFields, name, mobile, addhar_number, address):
    data = []
    if mobile != '':
        try:
            comd = ("Select * from customer where phone_no = " + str(mobile) + ";")
            print(comd)
            cursor.execute(comd)
            data = cursor.fetchall()
        except Exception:
            print("There is a exception in find if customer exists ?: {0}".format(e))
        if len(data) > 0:
            return

        if name != '' and mobile != '':
            try:
                if addhar_number == '':
                    addhar_number = 1234
                if address == '':
                    address = 'BBSR'
                comd = (
                        "INSERT INTO customer(cust_name, phone_no, address, addhar_number) VALUES(" + "'" + name + "',"
                        + mobile + ",'" + address + "'," + str(addhar_number) + ");")
                print(comd)
                cursor.execute(comd)
                mysqlDB.commit()
            except Exception as e:
                print("There was a exception while entering into database CUSTOMER : {0}".format(e))


# important
def saveGstData(weight, ornament, gold_rate, total_val, cgst, sgst, net_total, bill_no):
    try:
        comd = (
                "INSERT INTO gst_table(ornament, qty,weight,gold_rate, total_val, cgst, sgst, net_total, bill_no) VALUES('"
                + ornament + "'," + str(1) + "," + str(weight) + "," + str(gold_rate) + "," + str(total_val) + "," +
                str(cgst) + "," + str(sgst) + "," + str(net_total) + "," + str(bill_no) + ");"
        )
        print(comd)
        cursor.execute(comd)
        mysqlDB.commit()
    except Exception as e:
        messagebox.showerror("Error", "Error in save GST Data : {0}".format(e))
        print("There was a exception in save GST Data")


def findByNumber(number):
    try:
        comd = ("Select * from customer where phone_no = " + str(number) + ";")
        print(comd)
        cursor.execute(comd)
        data = cursor.fetchall()
        if len(data) == 0:
            return 0
        cust_data = []
        for i in data:
            cust_data.append(i)
        return cust_data[0]
    except Exception as e:
        print("there is a exception in findbynumber : {0}".format(e))


def findBillNumber():
    try:
        comd = "select id from BillTable order by id desc limit 1;"
        print(comd)
        cursor.execute(comd)
        # cursor.fetchall()
        result = cursor.fetchone()
        if (result == None):
            return 1

        return result[0]+1
    except Exception as e:
        print("there is a error in findbillnumber : {0}".format(e))


def saveBillLocation(u: UiFields):
    if u.mobile_txt.get() != '':
        try:
            cursor.execute('select id from customer where phone_no = ' + str(u.mobile_txt.get()) + ';')
            check = cursor.fetchone()
            if check is not None:
                u.customer_id = check[0]
            else:
                cursor.execute('select id from customer order by id desc Limit 1')
                u.customer_id = cursor.fetchone()[0]
        except Exception:
            u.customer_id = 1
            print("Error in saveBillLocation in finding customer_id")
    try:
        u.saveLocation = u.saveLocation.replace("\\", '\\\\')
        print(u.saveLocation)
        comd = ("INSERT INTO BILLTable(bill_location, customer_id) VALUES('" + u.saveLocation + "'," +
                str(u.customer_id) + ");")
        print(comd)
        cursor.execute(comd)
        mysqlDB.commit()
    except Exception as e:
        print("Error in saveBill in saving : {0}".format(e))


# important
def findGst(u: UiFields):
    try:
        comd = "Select id, added_date, ornament, qty, weight, gold_rate, total_val, cgst, sgst, net_total from gst_table where added_date between '" + str(u.cal1) + "' and '" + str(u.cal2) + "' and deleted = false;"
        print(comd)
        cursor.execute(comd)
        result = cursor.fetchall()
        create(result, u)
        if len(result):
            comd = "Select sum(total_val), sum(cgst),sum(sgst), sum(net_total) from gst_table where added_date " \
                   "between '" + str(u.cal1) + "' and '" + str(u.cal2) + "' and deleted = false;"
            print(comd)
            cursor.execute(comd)
            res = cursor.fetchall()
            if len(res):
                insertTotal(res, u)
    except Exception as e:
        messagebox.showerror("Error", "Error in finding GST Data : {0}".format(e))
        print("There is an error in finding gst data")


def saveGoldRate(u: UiFields):
    try:
        comd = ("INSERT INTO daily_gold_rate(gold_rate) VALUES(" + str(u.gold_rate) + ");")
        print(comd)
        cursor.execute(comd)
        mysqlDB.commit()
    except Exception as e:
        print("Error in saving into gold rate : {0}".format(e))


# important
def findGoldRate(u: UiFields):
    try:
        comd = "SELECT gold_rate from daily_gold_rate order by id desc limit 1"
        print(comd)
        cursor.execute(comd)
        result = cursor.fetchone()
        if result is None:
            u.gold_rate = 4876
        else:
            u.gold_rate = int(result[0])
    except Exception as e:
        messagebox.showerror("Error", "Error in save GST Data : {0}".format(e))
        print("Error in finding gold rate")


def findGRDate(u: UiFields):
    try:
        comd = ("SELECT gold_rate from daily_gold_rate WHERE added_date = '" + str(
            u.cal1) + "' ORDER BY id desc LIMIT 1;")
        print(comd)
        cursor.execute(comd)
        result = cursor.fetchall()
        if len(result) == 0:
            u.grRateOnDate = 0.0
        else:
            u.grRateOnDate = result[0][0]
    except Exception as e:
        print("There is a error in finding gold rate by date: {0}".format(e))


def findConfigValue(key):
    try:
        comd = ("select valuee from config where keyy = '" + str(key) + "';")
        print(comd)
        cursor.execute(comd)
        result = cursor.fetchone()
        print(result[0])
        return result[0]
    except Exception as e:
        messagebox.showerror("Error", "There is an exception in config:{0}".format(e))
        print("There is an exception in config:{0}".format(e))


def findAllConfig():
    try:
        comd = "Select keyy,valuee from config;"
        print(comd)
        cursor.execute(comd)
        result = cursor.fetchall()
        return result
    except Exception as e:
        print("There is a error in finding all config: {0}".format(e))


def insertNewConfig(c: UiFields):
    try:
        if c.newConfig_key.get() != '' and c.newConfig_key.get() != '':
            comd = ("Insert into config(keyy,valuee) Values('" + str(c.newConfig_key.get()) + "','" + str(
                c.newConfig_value.get()) + "');")
            print(comd)
            cursor.execute(comd)
            mysqlDB.commit()
    except Exception as e:
        print("There is a error in new config: {0}".format(e))
        messagebox.showerror("Error", "There is a error in new config: {0}".format(e))


def changeConfig(key, val):
    try:
        comd = ("UPDATE config SET valuee = '" + val + "' WHERE keyy = '" + key + "';")
        print(comd)
        cursor.execute(comd)
        mysqlDB.commit()
    except Exception as e:
        print("There is a error in editing config: {0}".format(e))
        messagebox.showerror("Error", "There is a error in editing config: {0}".format(e))


def findBillData():
    try:
        comd = 'SELECT c.id, c.cust_name, c.phone_no, b.billing_date, b.id, b.bill_location, b.deleted FROM billtable as b inner join customer as c on b.customer_id = c.id where deleted <> true;'
        print(comd)
        cursor.execute(comd)
        return cursor.fetchall()
    except Exception as e:
        print("There is a error in finding bill: {0}".format(e))
        messagebox.showerror("Error", 'There is a error in finding bill: {0}'.format(e))
        
        
def findBillDataByfilter(filter_name, filter):
    try:
        if filter_name == 'number':
            comd = 'SELECT c.id, c.cust_name, c.phone_no, b.billing_date, b.id, \
                b.bill_location, b.deleted FROM billtable as b inner join customer as c on\
                    b.customer_id = c.id having c.phone_no=' + str(filter) + ' and deleted <> true order by b.billing_date;'
        
        elif filter_name == 'name':
            comd = "SELECT c.id, c.cust_name, c.phone_no, b.billing_date, b.id, \
                    b.bill_location, b.deleted FROM billtable as b inner join customer as c on\
                        b.customer_id = c.id having c.cust_name='" + filter + "' and deleted <> true order by b.billing_date;"
        elif filter_name == 'bill_no':
            comd = 'SELECT c.id, c.cust_name, c.phone_no, b.billing_date, b.id, \
                b.bill_location, b.deleted FROM billtable as b inner join customer as c on\
                    b.customer_id = c.id having b.id=' + str(filter) + ' and b.deleted <> true;'
        elif filter_name == 'date':
            comd = "SELECT c.id, c.cust_name, c.phone_no, b.billing_date, b.id, \
                    b.bill_location, b.deleted FROM billtable as b inner join customer as c on\
                        b.customer_id = c.id having b.billing_date >= '" + filter + "' and deleted <> true order by b.billing_date desc;"
                
        print(comd)
        cursor.execute(comd)
        return cursor.fetchall()
    except Exception as e:
        print("There is a error in finding bill by filter: {0}".format(e))
        messagebox.showerror("Error", 'There is a error in finding bill by filter: {0}'.format(e))


def getPhNumber():
    try:
        comd = 'Select id, cust_name, phone_no from customer;'
        print(comd)
        cursor.execute(comd)
        result = cursor.fetchall()
        data = []
        for i in range(len(result)):
            comd = "Select billing_date from billtable where customer_id = " + str(result[i][0]) + " order by billing_date desc limit 1;"
            cursor.execute(comd)
            data.append((result[i][1], result[i][2], cursor.fetchone()[0]))

        return data
    except Exception as e:
        print("There is a exception : {0}".format(e))
        
def findBillTotal(bill_no):
    try:
        comd = "select  GROUP_CONCAT(ornament) as ornaments, sum(net_total) from gst_table group by (bill_no) having bill_no=" + str(bill_no) + ";"
        print(comd)
        cursor.execute(comd)
        result = cursor.fetchone()
        return result
    except Exception as e:
        print("There is a exception in finding bill total: {0}".format(e))
    

def bill_delete(bill_no):
    cursor1 = mysqlDB.cursor()
    try:
        print(bill_no)
        gst_table_ids = []
        comd = "select id from gst_table where bill_no = "+ bill_no + ";"
        print(comd)
        cursor1.execute(comd)
        result = cursor1.fetchall()
        comd = "Update billtable SET deleted = true WHERE id = "+ bill_no + ";"
        print(comd)
        cursor1.execute(comd)
        mysqlDB.commit()
        print(result)
        for gst_id in result:
            comd = "Update gst_table SET deleted = true WHERE id = " + str(gst_id[0]) + ";"
            cursor1.execute(comd)
            mysqlDB.commit()
    except Exception as e:
        messagebox.showerror("Error", 'There is a error in deleting bill: {0}'.format(e))
        mysqlDB.rollback()
    