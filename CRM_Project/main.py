import json
import clases


import Register
import login
def main():
    enter = input("""
        1. Login
        2.Register
    """)
    if enter == "1":
        return login.Login_check()
    elif enter == "2":
        return Register.Register()
    else:
        print("Xatoli !")
        return main()

if __name__ == "__main__":
    main()

