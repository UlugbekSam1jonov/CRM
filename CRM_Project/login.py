
import json
import admin_page
import user_page


def Login_check():
    print("Login Page")
    username = input("Useraname ")
    password = input("Password ")
    with open("Data/users.json","r") as file:
        data = json.load(file)
        for i in data["users"]:
            if i["username"] == username and i["password"] == password:
                print(i["status"])
                if i["status"] == 1:
                    return admin_page.admin(username,password)
                else:
                    return user_page.user(username,password)
                return main_page(username,password)
            break
        print("-----------------------")
        print("Eror")
        print("----------------------")

        return Login_check()
