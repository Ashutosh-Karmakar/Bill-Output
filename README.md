# Bill-Output

```
mysql
```

```
mysql.connector
```

```
win32api
```

```
win32print
```

```
tkinter
```

```
tkcalendar
```

```
datetime
```

```
openpyxl
```

```
sys
```

```
pyautogui
```

```
os
```

```
threading
```

```
tkcalendar.calendar_
```

```
babel
```

```
babel.numbers
```

```
xlwings
```

```
xlwings.constants
```

```
tkinter.messagebox
```

```
tkinter.simpledialog
```

```
email.mime.multipart
```

```
email.mime.text
```

```
email.mime.application
```

```
smtplib
```


# Creating Table From start:
```
Create database shop;

use shop;

CREATE TABLE customer(
  id INT AUTO_INCREMENT,
  cust_name VARCHAR(50),
  phone_no VARCHAR(11),
  address VARCHAR(100),
  addhar_number VARCHAR(15),
  PRIMARY KEY(id)
);

CREATE TABLE gst_table(
  id INT AUTO_INCREMENT,
  added_date DATETIME DEFAULT(CURRENT_DATE),
  ornament VARCHAR(50),
  qty INT,
  weight DECIMAL(10,5),
  gold_rate DECIMAL(10,2),
  total_val DECIMAL(30,10),
  cgst DECIMAL(10,5),
  sgst DECIMAL(10,5),
  net_total DECIMAL(30,10),
  bill_no INT NOT NULL DEFAULT 0,
  deleted BOOLEAN NOT NULL DEFAULT false,
  PRIMARY KEY(id)
);

CREATE TABLE billtable(
  id INT AUTO_INCREMENT,
  bill_location VARCHAR(100),
  billing_date DATETIME DEFAULT(curdate()),
  customer_id INT,
  deleted boolean NOT NULL DEFAULT false,
  PRIMARY KEY(id),
  FOREIGN KEY (customer_id) REFERENCES customer(id)
);

CREATE TABLE daily_gold_rate(
  id INT AUTO_INCREMENT,  
  added_date DATETIME DEFAULT(curdate()),
  gold_rate DECIMAL(10,2),
  PRIMARY KEY(id)
);

CREATE TABLE config(
  id INT AUTO_INCREMENT,
  keyy varchar(100),
  valuee varchar(100),
  PRIMARY KEY(id)
);
  
INSERT INTO config
  (keyy,valuee) 
  VALUES  
  ("BASEDIR_BILL","E:\Testing\testing_bill_store\Bill"),
  ("BASEDIR_GST","E:\Testing\testing_bill_store\Gst"),
  ('email_sender_address',"ashutoshkarmakar73@gmail.com"),
  ('email_receiver_address','ashutoshkarmakar72@gmail.com'),
  ('email_from_pass','Ashu@1999'),
  ('credit_card','2.1'),
  ('debit_card','1.4'),
  ('bg_color','#FFE6BC');
```

# make changes to current :
```

ALTER TABLE gst_table Modify weight DECIMAL(10,5);
ALTER TABLE gst_table Modify total_val DECIMAL(30,10);
ALTER TABLE gst_table Modify cgst DECIMAL(10,5);
ALTER TABLE gst_table Modify sgst DECIMAL(10,5);
ALTER TABLE gst_table Modify net_total DECIMAL(30,10);

-- 21-may-2022

ALTER TABLE gst_table ADD bill_no INT NOT NULL DEFAULT 0;
ALTER TABLE gst_table ADD deleted boolean NOT NULL DEFAULT false;
ALTER TABLE billtable ADD deleted boolean NOT NULL DEFAULT false;
```

