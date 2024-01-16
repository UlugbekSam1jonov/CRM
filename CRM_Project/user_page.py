import clases
from main import main


def profile(username, password):
    service = input("""
        Profile:
        1.Edit Name
        2.Edit Password
        3.Delete Profile
        4.Courses
        5.Delete Courses
        6.Balance
        0. Back
    """)
    if service == "1":
        pass
    elif service == "2":
        pass
    elif service == "3":
        pass
    elif service == "4":
        pass
    elif service == "5":
        pass
    elif service == "6":
        pass
    elif service == "0":
        pass
    else:
        print("Invalid")
        return profile(username, password)



def user(username,password):
    print("Welcome to the user page ")

    a = """
    1. Course
    2. Speciality
    3. Profil
    4. Log Out
    ------------
    """
    print(a)
    header = input(">> ")
    if header == "1":
        data = clases.Course.get_all_course()
        for i in data:
            print(f"""
                  Name: {i["name"]}
                  Graduation: {i["graduation"]}
                  Description: {i["description"]}
                  Buying users: {i["buying_users"]}
                  Price: {i["price"]}
                  Mentor: {i["mentor"]}
                  Hours: {i["hours"]}
                  Reyting: {i["reyting"]}
                  Lenguege: {i["lenguege"]}
              """)
            print("_________________________________________\n")
        return user(username, password)


    elif header == '2':
        data = clases.Speciality.get_all_Speciality()
        for i in data:
            print(f"""
            Name: {i["name"]}
            Description: {i["description"]}
            graduation: {i["graduation"]}
            create_date: {i["create_date"]}           
            """)

            print("----------------------")
        return user(username,password)

    elif header == '3':
        return profile(username, password)



    elif header == '0':
        return main
    else:
        print("Invalid")
        return user(username,password)

