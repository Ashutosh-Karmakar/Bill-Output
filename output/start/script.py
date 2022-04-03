import os

Base = r'D:\1 FINAL SHOP BILL\shopbill\FrontEnd'
# print(os.listdir())
# for dir in os.listdir():
#     if dir.endswith('.py'):
#         print(os.path.join(Base, dir))


packages = ["mysql", "mysql.connector", "win32api", "win32print", "tkinter",
            "tkcalendar", "datetime", "openpyxl", "sys", "pyautogui", "os", "threading", 
            "Pillow", "babel", "babel.numbers", "tkcalendar.calendar_", "tkinter.messagebox", 
            "tkinter.simpledialog", "smtplib", "email"]

output = r'D:\1 FINAL SHOP BILL\shopbill\FrontEnd\start.py'

comd = "pyinstaller --noconfirm --onedir --console "
print(os.path.join(Base,'start.py'))
for dir in os.listdir():
    print(dir)
    if dir.endswith(('.py','.png','.jpeg','.jpg')) and dir != 'start.py':
        print(dir)
        comd = comd + '--add-data "' +os.path.join(Base, dir) + '";. '

for pkg in packages:
    comd = comd +'--hidden-import "' + pkg + '" '
    
comd = comd + '"' + output + '" '


print(comd)
os.system(comd)
'''
pyinstaller --noconfirm --onedir --console 
--add-data "E:/other/shopDir/shopbill/FrontEnd/__init__.py;." 
--add-data "E:/other/shopDir/shopbill/FrontEnd/backend.py;." 
--add-data "E:/other/shopDir/shopbill/FrontEnd/baseIntialization.py;." 
--add-data "E:/other/shopDir/shopbill/FrontEnd/billgenerator.py;." 
--add-data "E:/other/shopDir/shopbill/FrontEnd/database.py;." 
--add-data "E:/other/shopDir/shopbill/FrontEnd/findBill.py;." 
--add-data "E:/other/shopDir/shopbill/FrontEnd/findGoldrate.py;." 
--add-data "E:/other/shopDir/shopbill/FrontEnd/goldrate.py;." 
--add-data "E:/other/shopDir/shopbill/FrontEnd/hallmark.png;." 
--add-data "E:/other/shopDir/shopbill/FrontEnd/monthlyGST.py;." 
--add-data "E:/other/shopDir/shopbill/FrontEnd/printer.py;." 
--add-data "E:/other/shopDir/shopbill/FrontEnd/shopLogo.png;." 
--hidden-import "mysql" 
--hidden-import "mysql.connector" 
--hidden-import "win32api" 
--hidden-import "win32print" 
--hidden-import "tkinter" 
--hidden-import "tkcalendar" 
--hidden-import "datetime" 
--hidden-import "openpyxl"
--hidden-import "sys" 
--hidden-import "pyautogui" 
--hidden-import "os" 
--hidden-import "threading" 
--hidden-import "Pillow" 
--hidden-import "babel" 
--hidden-import "babel.numbers" 
--hidden-import "tkcalendar.calendar_" 
--hidden-import "tkinter.messagebox" 
--hidden-import "tkinter.simpledialog"  
"E:/other/shopDir/shopbill/FrontEnd/start.py"
'''

# pyinstaller --noconfirm --onedir --console --add-data "D:/1 FINAL SHOP BILL/shopbill/FrontEnd/__init__.py;." --add-data "D:/1 FINAL SHOP BILL/shopbill/FrontEnd/backend.py;." --add-data "D:/1 FINAL SHOP BILL/shopbill/FrontEnd/baseIntialization.py;." --add-data "D:/1 FINAL SHOP BILL/shopbill/FrontEnd/billgenerator.py;." --add-data "D:/1 FINAL SHOP BILL/shopbill/FrontEnd/changeConfig.py;." --add-data "D:/1 FINAL SHOP BILL/shopbill/FrontEnd/database.py;." --add-data "D:/1 FINAL SHOP BILL/shopbill/FrontEnd/findBill.py;." --add-data "D:/1 FINAL SHOP BILL/shopbill/FrontEnd/findGoldrate.py;." --add-data "D:/1 FINAL SHOP BILL/shopbill/FrontEnd/goldrate.py;." --add-data "D:/1 FINAL SHOP BILL/shopbill/FrontEnd/gstexel.py;." --add-data "D:/1 FINAL SHOP BILL/shopbill/FrontEnd/hallmark.png;." --add-data "D:/1 FINAL SHOP BILL/shopbill/FrontEnd/monthlyGST.py;." --add-data "D:/1 FINAL SHOP BILL/shopbill/FrontEnd/printer.py;." --add-data "D:/1 FINAL SHOP BILL/shopbill/FrontEnd/script.py;." --add-data "D:/1 FINAL SHOP BILL/shopbill/FrontEnd/shopLogo.png;." --add-data "D:/1 FINAL SHOP BILL/shopbill/FrontEnd/start.py;."  --hidden-import "mysql" --hidden-import "mysql.connector" --hidden-import "win32api" --hidden-import "win32print" --hidden-import "tkinter" --hidden-import "tkcalendar" --hidden-import "datetimeopenpyxl" --hidden-import "sys" --hidden-import "pyautogui" --hidden-import "os" --hidden-import "threading" --hidden-import "Pillow" --hidden-import "babel" --hidden-import "babel.numbers" --hidden-import "tkcalendar.calendar_" --hidden-import "tkinter.messagebox" --hidden-import "tkinter.simpledialog" --hidden-import "smtplib" --hidden-import "email"  "D:/1 FINAL SHOP BILL/shopbill/FrontEnd/start.py"