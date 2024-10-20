#Theme function 

#1 function
def son(x, y):
    if x>0 and y>0:
        print(f"{x} + {y} = {x+y}")
    else:
        print("Siz manfiy son kiritdingiz ! ")
        
t=son(10, 10)

# 2 function
def ismTop(ism):
    if ism=="Diyor":
        print("Saytga xush kelibsiz! ")
    else:
        print("Siz saytga kirishingiz mumkin emas! ")
        

p=ismTop("Diyor")
# 3 function

"""

mashinalarning 
matorini
topuvchi
funksiya

"""

def mator(mashina):
    """ Bu funksiya mashinalarning mator hajmini ekranga chiqarib beradi """
    if mashina.lower()=="jentra":
        print(f"{mashina.lower()} ning mator hajmi --> 1.5l")
    elif mashina=="damas":
        print(f"{mashina.lower()} ning mator hajmi --> 0.8l")
    elif mashina=="malibu":
        print(f"{mashina.lower()} ning mator hajmi --> 2.0l")
    else:
        print(f"{mashina.lower()} mashinasi afsuski bizning bazamizda mavjud emas! ")
    
j1=mator("malibu")
j2=mator("damas")
j3=mator("nexia")
j4=mator("jentra")
j5=mator("matiz")



# 4 funksiya


"""
yoshini
kiritib
yilini 
topish funksiyasi
"""

def yosh(x):
    """ Tug'ilgan yilini topish formulasi """
    print(f"Sizning tug'ilgan yilingiz {2024-x}")

d1=yosh(16)
d2=yosh(15)
d3=yosh(17)

# 5 funksiya
"""
user 
kirishi 
uchun 
funksiya
"""


def user(name, password):
    """ Useringizga kiruvchi funksiya """
    if name=="User" and password=="user123":
        print(f"{name} siz akkauntingizga kirdingiz!")
    elif name=="User1" and password=="user321":
        print(f"{name} siz akkauntingizga kirdingiz!")
    else:
        print(f"{name} afsuski siz akkauntingizga kira olmadingiz, iltimos qayta urinib ko'ring")
        
        
u1=user("User1", "user123")
u1=user("User", "user123")
u1=user("User", "user321")
u1=user("User1", "user321")


# 5 funksiya

"""
sonlar 
o'rta
arifmetgini
topish
"""

def ortaQiymat(x, y, z):
    """O'rta arifmetik topuvchi funksiya"""
    a=x+y+z
    b=a//3
    print(b)
    
z=ortaQiymat(2, 3, 4)


# 6 funksiya

"""
hayvonlarni 
qanday
hayvon 
ekanligini
qaytaruvchi
funksiya
"""

def animal(hayvon):
    """ Hayvon funksiyasi """
    if hayvon=="kuchuk":
        print(f"{hayvon} uy hayvoni")
    elif hayvon=="bo'ri":
        print(f"{hayvon} yovvoyi hayvon")
    elif hayvon=="mushuk":
        print(f"{hayvon} uy hayvoni")
    elif hayvon=="yo'lbars":
        print(f"{hayvon} yovvoyi hayvon")
    else:
        print(f"{hayvon} qanday hayvonligini tushunmadim")
        
anmal1=animal("kuchuk")
anmal2=animal("mushuk")
anmal3=animal("bo'ri")
anmal4=animal("yo'lbars")
anmal5=animal("tulki")


# 1-funksiya
"""
funksiya 
2 qiymat
ustida
4 amal bajarishi
lozim
"""

def amal1(a,b):
    """ 4 amal bajaruvchi funksiya """
    print(f"{a} + {b} = {a+b}")
    print(f"{a} - {b} = {a-b}")
    print(f"{a} * {b} = {a*b}")
    print(f"{a} / {b} = {a/b}")
    
natija=amal1(10, 11)

# 2-funksiya
"""
funksiya username
phone number password
qabul qilsin
va ular to'g'ri bo'lsa
saytga kirdingiz
aks holda kira olmadingiz
deb chiqarsin
"""

def login(name, phoneNumber, password):
    """ Simply login form function """
    if name.lower()=="user" and phoneNumber==953210571 and password.lower()=="user123":
        print("Siz saytga kirdingiz !")
    elif name.lower()=="admin" and phoneNumber==974103655 and password.lower()=="admin123":
        print("Siz saytga kirdingiz !")
    elif name.lower()=="root" and phoneNumber==951763655 and password.lower()=="root123":
        print("Siz saytga kirdingiz !")
    else:
        print("Afsuski saytga kira olmadingiz, kiritilgan maydonlarni to'g'riligini tekshiring! ")
        
lgin1=login("user", 953210571, "user321")
lgin2=login("user", 953210573, "user123")
lgin3=login("user1", 953210571, "user123")
lgin4=login("user", 953210571, "user123")

# 3-funksiya
"""
funksiyada email kiritsin
agar email son va alifbo
kiritgan bo'lsa o'tkazsin
aks xolda xato
"""

def email(x):
    """ Email checker function """
    if x.isalnum():
        print("Siz saytga kirdingiz")
    else:
        print("Siz saytga kira olmadingiz")
    
mail=email("sadada12asdas1221")

# 4-funksiya
"""
100 yoshgacha 
nechi yil
borligini hisoblash
"""

def year(years):
    """ how much years to 100 """
    b=2024-years
    print(f"Siz 100 yoshga to'lishingiz uchun {100-b}")
    
yr=year(12)
yr1=year(13)
yr3=year(28)



def avto(mashina):
    """ Bu funksiya sizning mashinangizning rangini chiqarib beradi """
    if mashina.lower() == "nexia":
        print(f'Sizning {mashina.upper()}ngizning rangi oq')
    elif mashina.lower() == "cobalt":
        print(f'Sizning {mashina.upper()}ngizning rangi kulrang')
    elif mashina.lower() == "damas":
        print(f'Sizning {mashina.upper()}ngizning rangi yashil')
    elif mashina.lower() == "gentra":
        print(f'Sizning {mashina.upper()}ngizning rangi qora')
    else:
        print("Bu mashina afsuski bazamizda mavjud emas! ")


q1 = avto("Gentra")
q2 = avto("Nexia")
q3 = avto("Cobalt")
q4 = avto("Damas")


def kabisaYili(yil):
    """ Kabisa yilini topish """
    if yil % 4 == 0:
        print('Bu yil kabisa yili')
    else:
        print('Bu yil kabisa yili emas')


y1 = kabisaYili(2025)
y2 = kabisaYili(2036)
y3 = kabisaYili(1988)


def amal1(son):
    """ Juft va toq sonlarni aniqlash """
    if son % 2 == 0:
        print('Bu son juft son')
    elif son % 2 == 1:
        print('Bu son toq son')
    else:
        print('Xatolik yuz berdi')


s1 = amal1(14)
s2 = amal1(56)
s3 = amal1(73)


f = []


def meva(fruit):
    """ mevalar funksiyasi """
    if fruit == "Olma":
        f.append(fruit)
        print(f)
    elif fruit == "Anor":
        f.append(fruit)
        print(f)
    elif fruit == "Uzum":
        f.append(fruit)
        print(f)
    elif fruit == "Olcha":
        f.append(fruit)
        print(f)
    elif fruit == "Gilos":
        f.append(fruit)
        print(f)
    else:
        print(f"{fruit} --> meva emas")


r1=meva("Olma")








luxClass=[]
economClass=[]



def msh(car):
    """ mashina funksiya """
    if car=="Porsche" or "BMW" or "Mers":
        luxClass.append(car)
        print(luxClass)
    elif car=="Gentra" or "Malibu" or "Tahoe":
        economClass.append(car)
        print(economClass)
    else:
        print("Xatolik! ")


a1=msh("Malibu")
a1=msh("Gentra")
a1=msh("BMW")
a1=msh("Tahoe")
a1=msh("Porsche")
a1=msh("Mers")
6
