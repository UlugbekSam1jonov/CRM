import clases
from login import Login_check


def Register():
    print("Register Page")
    print("Royhatdan o'tish uchun quydagilarni to'ldiring")
    f_name = input("First name ")
    l_name = input("Last name")
    useename = input("Username ")
    password = input("Password")
    password2 = input("Password2 ")
    while password != password2:
        print("PASSWORD BIR XIL BO'LISHI KERAK")
        password = input("Password ")
    gmail = input("Gmail ")

    if password == password2:
        register = clases.Register(useename,password,f_name,l_name,gmail,0)
        print("Succesfull")
        register.save_data_user()
        return Login_check()