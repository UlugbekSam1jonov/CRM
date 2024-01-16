from  datetime import datetime
import json
class Login:
    """Bu class kirish classi va u User clasidan voris oladi"""
    def __init__(self,user_name,password):
       self.username = user_name
       self.password = password
User1 = Login("Ulugbek","2205")


class User (Login):
    """Bu class User haqida"""
    id = 1
    def __init__(self,user_name,password,f_name,l_name,gmail,status :bool):
        Login.__init__(self,user_name,password)
        self.id = User.id
        self.f_name = f_name
        self.l_name = l_name
        self.gmail = gmail
        self.status = status

        self.create_date = datetime.now()
        User.id += 1

    def __str__(self):
        return f"{self.id},{self.username}, {self.password}, {self.f_name}, {self.l_name}, {self.gmail}, {self.status}, {self.create_date}"

Person_1 = User("Ulugbek","2205","Ulugbek","Samijonov","samijinov@gamil.com","O'quvchi")
Person_2 = User("Ulugbek","2205","Ulugbek","Samijonov","samijinov@gamil.com","O'quvchi")
Person_3 = User("Ulugbek","2205","Ulugbek","Samijonov","samijinov@gamil.com","O'quvchi")
print(Person_1)
print(Person_2)
print(Person_3)



class Register (User):
    """Bu class shahsnining ma'lumotlarini o'zida jamlaydi"""
    id = 1
    def __init__(self,user_name,password,f_name,l_name,gmail,status):
        User.__init__(self,user_name,password,f_name,l_name,gmail,status)
        self.id = Register.id
    def save_data_user(self):
        with open("Data/users.json","r") as file:
            data = json.load(file)
            new_user = {
                "id ":self.id,
                "username":self.username,
                "password": self.password,
                "first_name": self.f_name,
                "last_name": self.l_name,
                "gmail":self.gmail,
                "status":self.status,
                "create_date": "fsgsfgas"
            }
            data["users"].append(new_user)
        with open("Data/users.json","w") as f:
            json.dump(data,f)

class Student(User):
    """Bu classda o'quvchi haqidagi ma'lumotlar saqalanadi va u student clasidan voris oladi"""
    def __init__(self,user_name,password,f_name,l_name,gmail,status: 0,courses : list):
        User.__init__(self,user_name,password,f_name,l_name,gmail,status)
        self.courses = []



class Speciality:
    """Bu class kurs davomida nimalarni or'ganish haqida ma'lumot beradi"""
    def __init__(self,name,description,gradution):
        self.name =name
        self.description =description
        self.graduatuion = gradution
        self.crate_datae = datetime.now()


    @staticmethod
    def get_all_Speciality():
        with open("Data/speciality.json","r") as file:
            data = json.load(file)

            return data["speciality"]



class Course:
    """Bu class kurs haqida ma'lumot"""

    def __init__(self,CourseName,Continue,Skils,price,PupilsCount,Mentor,Language):
        self.CourseName = CourseName
        self.Continue = Continue
        self.Skils = Skils
        self.price = price
        self.PupilCount = PupilsCount
        self.Mentor =Mentor
        self.Language = Language
        self.creation_date = f"{datetime.now().year}-{datetime.now().month}-{datetime.now().day}"
    def get_info(self):
        return f"Kurs haqida ma'lumot {self.CourseName},{self.Continue},{self.Skils},{self.price},{self.PupilCount},{self.Language},{self.Mentor}"
    @staticmethod
    def get_all_course():
        with open("Data/courses.json","r") as file:
            data = json.load(file)
            return data["courses"]


Student1 = Course("Python","8 oy","Pandas,Numpy,Django,Git","1320ming so'm","25","jfee","fsgfasf")

class Modul:
    """Bu class Modul haqida ma'lumot """
    id = 1
    def __init__(self,Name,ModulCount,LessonCount,price,description,):
        self.id = Modul
        self.name = Name
        self.ModulCount = ModulCount
        self.LessonCount = LessonCount
        self.price = price
        self.description = description
        self.createdate = datetime.now()
        Modul.id += 1

    def get_info(self):
        return f"Kurs haqida ma'lumot {self.name},{self.ModulCount},{self.LessonCount},{self.price}"

class Mentor:
    """Bu class mentor haqida """
    def __init__(self,f_name,l_name,experience,Level,Subject,password,status):
        self.f_name = f_name
        self.l_name = l_name
        self.experience = experience
        self.level = Level
        self.Subject = Subject
        self.password = password
        self.status = status

    def get_info_Mentor(self):
        return f"Ustoz haqida ma'lumot {self.f_name},{self.l_name},{self.experience},{self.level}.{self.Subject},{self.password},{self.status}"

Info = Mentor("Muhammadjon","Muminov","5yil","Midle plus","Python","2205","Mentor")


class Lesson:
    id = 1
    """Bu class darslar haqida"""
    def __init__(self,name,resurs,format,homework:"None",sort):
        self.id = Lesson
        self.name = name
        self.resurs = resurs
        self.video = format
        self.homework = homework
        self.sort = sort
        self.date = datetime.now().date()
        Lesson.id += 1

    def get_info_Lesson(self):
        return f"Bu darslar haqida malumot {self.name},{self.resurs},{self.video},{self.homework},{self.sort}"

class Filial:
    """Bu class filial haqida """
    def __init__(self,name,location,workTime,size):
        self.name = name
        self.location = location
        self.workTime = workTime
        self.size = size

    def get_info_Filia(self):
        return f""




