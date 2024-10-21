# python back-end
# 5 first_letter nomli lambda funksiya yarating va u berilgan so'zning birinchi harfini qaytarsin
lambda first_letter:print('first_letter'[0])
# 6  5 last_letter nomli lambda funksiya yarating va u berilgan so'zning oxirgi harfini qaytarsin
lambda last_letter:print('last_letter'[-1])
# 7 first_last nomli lambda funksiya yarating va u berilgan so'zning oxirgi va bosh harflarini qaytarsin
# lambda first_last:print('first_last'[0,-1])
# 8 daraja hisoblang. Foydalanuvchi x va n sonlarini kiritsin va x ning n inchi darajasini hisoblasin
def darajaQoyish(x, n):
    """ Bu daraja hisoblaydigan funksiya """
    print(f"{x} ning {n} inchi darajasi => {x**n}")

darajaQiymat=darajaQoyish(2, 3)
# 9 1 dan 10 gacha bo'lgan sonlar ro'yxatini for va while orqali chiqaring
numberList=[1,2,3,4,5,6,7,8,9,10]
for n in numberList:
    print(n)
    


i = 1
while i < 11:
  print(i)
  if i == 11:
    break
  i += 1
  
# 10 foydalanuvchidan biror matn kiritishini so'rang va so'z nechta harfdan tashkil topganini chiqaring
sozKiriting=input("Biron-bir so'z kiriting > ")
print(len(sozKiriting))

# 11 foydalanuvchidan ism va yosh kiritishini so'rang va uni lug'at ko'rinishida saqlang
a={}
ism=input("Ismingizni kiriting> ")
yosh=int(input("Yoshingizni kiriting> "))
a[ism]=yosh
print(a)

# 12 Ikkita  ixtiyoriy  ro’yxat tuzing  va ikkala ro’yxatni solishtiring   ikkita royxatdaham mavjud sonlarni konsolga chiqaring
list1=[12,8545,8465,51,151] 
list2=[12,545,845,51,1512] 
commonNumbers = list(set(list1) & set(list2))
print(commonNumbers)

# 13 Foydalanuvchidan masofani vaqtni so'rang agar u boradigan masofa 3 km dan ko’p va vaqt 10 daqiqadan  ko’p bo’lsa  sizga , taxi kerak yoki kerakmas deb xabar chiqaruvchi dastur tuzing :
def taxi(masofa, vaqt):
    if masofa>=3 and vaqt>=10:
        print("Sizga taxi kerak! ")
    else:
        print("Sizga taxi kerak emas! ")
        
r=taxi(4, 8)

# 14 Foydalanuvchidan yoshini, ismini, va emailini oling va agar u  18 yoshdan kichik bo'lsa, yoki emaili to'g'ri formatda bo'lmasa, xatolik xabarni chiqaring:
def yoshEmailIsm(Y, Email, I):
    if Y>=18 and Email.endswith("@gmail.com"):
        print("Siz saytga kirdingiz")
    else:
        print("Sizda xatolik mavjud")
        
yeiq=yoshEmailIsm(19, "bdiyorxasanov@gmail.com", "diyor")

# 15 Foydalanuvchidan son kiritishni so'rang va u kiritgan son toq yoki juftligini tekshiring
def tek(son):
    if son % 2 == 0:
        print("Bu son juft son")
    else:
        print("Bu son toq son")
        
qiymat=tek(12)

# 16 : Foydalanuvchidan kun raqamini kiritishni so'rang va u haftaning qaysi kuniga to'g'ri kelishi, chiqaring masalan
# 1 soni kiritsa   dushanba  

def kunHafta(son):
    if son==1:
        print("Dushanba")
    elif son==2:
        print("Seshanba")
    elif son==3:
        print("Chorshanba")
    elif son==4:
        print("Payshanba")
    elif son==5:
        print("Juma")
    elif son==6:
        print("Shanba")
    elif son==7:
        print("Yakshanba")
    else:
        print("Xatolik")

# 17 : Foydalanuvchi istalgan sonni kiritsin va kiritsa, uning darajasini hisoblaydigan dastur yozing yana yangi son kiritsa yana hisoblang  foydalanuvchi  exit  yozmaguncha takrorlang

savol=("Iltimos son kiriting \n\n")
savol+=("To'xtatish uchun (exit)")

while True:
    qiymat=input(savol)
    if qiymat=="exit":
        break
    else:
        print(f"Siz kiritgan sonning kvadrati {qiymat**2}")
    
# 18 my_list = [5, 2, 8, 1, 9]   teskari  tartibda chiqaring  ?
my_list = [5, 2, 8, 1, 9]
my_list.reverse()
print(my_list)

# 19  my_list = [3, 6, 2, 1, 7, 9]  Listdagi elementlarning o'rta qiymatini toping.
my_list = [3, 6, 2, 1, 7, 9]
print(sum(my_list) // len(my_list))

# 20 my_list = [4, 2, 7, 5, 9]  Listdagi elementlarning yig'indisini toping.
my_list = [4, 2, 7, 5, 9]
print(sum(my_list))

# 21 Listdagi eng kichik va eng katta elementlarni toping. my_list = [3, 8, 2, 6, 1, 9]
my_list = [3, 8, 2, 6, 1, 9]
print(max(my_list))
print( min(my_list))

# 22 Listdagi juft sonlarni ajratib oling.      my_list = [1, 5, 2, 8, 3, 7]
my_list = [1, 5, 2, 8, 3, 7]

# Juft sonlarni ajratish
even_numbers = [num for num in my_list if num % 2 == 0]
print(even_numbers)

# 23 Listdagi toq sonlarni ajratib oling. Listdagi juft sonlarni ajratib oling.
my_list = [1, 5, 2, 8, 3, 7]

# Juft sonlarni ajratish
even_numbers = [num for num in my_list if num % 2 == 1]
print(even_numbers)

# 24 Foydalanuvchidan ikki son kiritishni so'rang va kiritilgan sonlarning o'rta arifmetigini topuvchi dastur tuzing
a=int(input("1-sonni kiriting> "))
b=int(input("2-sonni kiriting> "))
c=a+b
print(f"{c//2}")

# 25 1 dan 100 gacha bo'lgan toq sonlarni yig'indisini hisoblayuvchi dastur tuzing:
# 1 dan 100 gacha bo'lgan toq sonlar yig'indisini hisoblaydigan dastur
odd_sum = sum(i for i in range(1, 101) if i % 2 == 1)
print(f"1 dan 100 gacha bo'lgan toq sonlar yig'indisi: {odd_sum}")

# 26 Foydalanuvchidan 3 ta son kiritishni so'rang va kiritilgan sonlardan eng kattasini topuvchi dastur tuzing:
def son(x, y, z):
    print(max(x, y, z))
    
s=son(25, 48, 78)

# 27 	1 dan 100 gacha sonlar ro'yxatini yaratib, undan 3ga qoldiqsiz bo'linadigan sonlarni chiqaring:
odd_sum = sum(i for i in range(1, 101) if i % 3 == 0)
print(f"1 dan 100 gacha bo'lgan toq sonlar yig'indisi: {odd_sum}")

# 28	Berilgan ro'yxatdagi elementlardan juftlarini ajratib olib yangi ro'yxatga saqlayuvchi dastur tuzing:
a=[12,151,151,54515,451]
b=[]

def hisobla(x):
    if a % 2 == 0:
        b.append(x)

f=hisobla(12)

# 29.	Berilgan ro'yxatdagi elementlarni yig'indisini topuvchi dastur tuzing:

a=[12,15641,1515,121]
b=sum(a)
print(b)

# 30. 30  “Hello world” matnini ekranga 10 marta chiqaring
print(f"Hello world")
print(f"Hello world")
print(f"Hello world")
print(f"Hello world")
print(f"Hello world")
print(f"Hello world")
print(f"Hello world")
print(f"Hello world")
print(f"Hello world")
print(f"Hello world")




def dominTek(domin):
    """ Bu domenlarni tekshirib beradi """
    if domin.endswith('.uz'):
        print("Bu Uzbekiston domini")
    
dominTek('dsfdsfds.ru')


def admin_tek(gmail,password):
    """ Bu funksiya adminning saytga kirish huquqi bor yoki yo'qligini tekshirib beradi"""
    if password==123 and gmail.startswith("admin") and gmail.endswith("@gmail.com"):
        print("Sizda adminlik huquqi bor")
    else:
        print("Sizda adminlik huquqi yo'q")



admin1=admin_tek("adminvali@gmail.com", 1234)
admin2=admin_tek("adminali@gmail.com", 123)
