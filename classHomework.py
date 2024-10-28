#1 User classini ochib uning ichiga 4ta xususiyat, 5ta funksiya va 3ta object yaratish

class User():
    def __init__(self, first_name, last_name, email, password):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password

    def get_first_name(self):
        return self.first_name

    def get_last_name(self):
        return self.last_name

    def get_email(self):
        return self.email

    def get_password(self):
        return self.password

    def get_all(self):
        return self.first_name, self.last_name, self.email, self.password

user1 = User('Diyor', 'Xasanov', 'bdiyorxasanov@gmail.com', '1234')
user2 = User('Ali', 'Valiyev', 'alivaliyev95@gmail.com', '0000')
user3 = User('Eshmat', 'Toshmatov', 'EshmatToshmatov_001@gmail.com', '5555')

print(user1.get_all())


#2 Televizorlar classini ochib uning ichiga 6ta xusisiyat, 5ta funksiya va 3ta object yaratish

class Television():
    def __init__(self, name, price, color, size, version, antenna):
        self.name = name
        self.price = price
        self.color = color
        self.size = size
        self.version = version
        self.antenna = antenna

    def get_name(self):
        return self.name

    def get_price(self):
        return self.price

    def get_color(self):
        return self.color

    def get_size(self):
        return self.size

    def get_version(self):
        return self.version


tv1 = Television("Samsung", 800, "black", "43", "smart", "kabel")
tv2 = Television("Shivaki", 800, "black", "32", "smart", "baraban")
tv3 = Television("LG", 800, "black", "54", "smart", "kabel")

print(tv1.get_price())

# 3 do'kon classini yaratib, uning ichiga 5ta xususiyat, 5ta funksiya va 4 ta object yaratib objectlarni hammasini ekranga chiqarish

class Shop():
    def __init__(self, location, size1, color1, number, type):
        self.location = location
        self.size1 = size1
        self.color1 = color1
        self.number = number
        self.type = type

    def get_location(self):
        return self.location

    def get_size1(self):
        return self.size1

    def get_color1(self):
        return self.color1

    def get_type(self):
        return self.type

    def get_number(self):
        return self.number

    def get_all1(self):
        return self.location, self.size1, self.color1, self.type, self.number

shop1 = Shop("Samarkand", "300*200", "red", "50-500-00-50", "electron")
shop2 = Shop("Samarkand", "200*150", "yellow", "90-444-77-88", "electron")
shop3 = Shop("Tashkent", "1000*800", "blue", "95-950-00-00", "electron")
shop4 = Shop("Tashkent", "900*750", "green", "99-999-11-12", "electron")

print(shop1.get_all1())
print(shop2.get_all1())
print(shop3.get_all1())
print(shop4.get_all1())

# 4 Maktab classini ochib uning ichiga 6 ta xususiyat, 7 ta funksiya, 4 ta object yaratish

class School():
    def __init__(self, loc, director, math_teacher, number_school, smart_student, mindless_student):
        self.loc = loc
        self.director = director
        self.math_teacher = math_teacher
        self.number_school = number_school
        self.smart_student = smart_student
        self.mindless_student = mindless_student

    def get_location(self):
        return self.loc

    def get_director(self):
        return self.director

    def get_math_teacher(self):
        return self.math_teacher

    def get_number_school(self):
        return self.number_school

    def get_smart_student(self):
        return self.smart_student

    def get_mindless_student(self):
        return self.mindless_student

    def get_all2(self):
        return self.loc, self.director, self.math_teacher, self.number_school, self.smart_student, self.mindless_student

school1 = School("Samarkand", "Azimjon", "Nigora", 2, "Damir", "Diyor")
school2 = School("Samarkand", "Ali", "Nigina", 10, "Amir", "Vali")
school3 = School("Samarkand", "Mashrab", "Nargiza", 1, "Eshmat", "Zuhra")
school4 = School("Samarkand", "Zafar", "Munis", 3, "Fotima", "Toshmat")
