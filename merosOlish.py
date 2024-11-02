# class Market():
#     def __init__(self,product,date,price,date_over):
#         self.product=product
#         self.date=date
#         self.price=price
#         self.date_over=date_over
#
#     def get_all(self):
#         return self.product,self.date,self.price,self.date_over
#
#
#
# class Pepsi(Market):
#
#     def get_price(self):
#         return self.price
#
#
#
# product1=Market("Pepsi",2024,12000,2025)
#
#
# print(product1.get_all())
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#









class User():
    def __init__(self, first_name, last_name, user_name, email, password, birthday):
        self.first_name = first_name
        self.last_name = last_name
        self.user_name = user_name
        self.email = email
        self.password = password
        self.birthday=birthday

    def get_first_name(self):
        return self.first_name

    def get_last_name(self):
        return self.last_name

    def get_user_name(self):
        return self.user_name

    def get_email(self):
        return self.email

    def get_password(self):
        return self.password

    def get_birthday(self):
        return self.birthday

    def get_all(self):
        return self.first_name, self.last_name, self.user_name, self.email, self.password, self.birthday


user1=User("Diyor", "Xasanov", "diyorkhasanov", "bdiyorxasanov@gmail.com" , 0000, 2009)
print(user1.get_all())


class Mebel():
    def __init__(self, rang, narx, material):
        self.rang = rang
        self.narx = narx
        self.material = material

    def get_hamma(self):
        return self.rang, self.narx, self.material

    def get_narx(self):
        return self.narx

    def get_rang(self):
        return self.rang

    def get_material(self):
        return self.material

mebel1=Mebel("qo'ng'ir", 2000, "mdf")

print(mebel1.get_hamma())




class Flower():
    def __init__(self, price, name, color, datetime):
        self.price = price
        self.name = name
        self.color = color
        self.datetime = datetime


    def get_price(self):
        return self.price

    def get_name(self):
        return self.name

    def get_color(self):
        return self.color


flower1=Flower(200000, "Lola", "qizil", 2025)
print(flower1.get_color())


class Tel():
    def __init__(self, marka1, narx1, rang1, zaryadchik1):
        self.marka1 = marka1
        self.narx1 = narx1
        self.rang1 = rang1
        self.zaryadchik1 = zaryadchik1


    def get_marka1(self):
        self.marka1



class Iphone(Tel):

    def get_tel(self):
        return  self.marka1, self.rang1, self.narx1, self.zaryadchik1




tel1 = Iphone('iphone 11', 500, 'qora', 'type a')
print(tel1.get_tel())
















































