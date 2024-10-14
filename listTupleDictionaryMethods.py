# №1 telefonlar ro'xatini tuzib ichiga 5 ta qiymat berish
tel=["Iphone", "Samsung", "Infinix", "Redmi", "Nokia"]
# 2 telefonlar ro'yxatidan biron birini tanlab u qiymat nechinchi indexda turganini aniqlash
index=tel.index("Samsung")
print(index)
# 3 o'sha ro'yxatdan biron telefon markasi nechi marta takrorganligini ko'rish
count=tel.count("Iphone")
print(count)
# 4 lisning orqasidan 2 ta qiymat qo'shish
tel.append("Novey")
tel.append("Maxvi")
print(tel)
# 5 listga 1 ta xoxlagan joyidan qiymat qo'shish
tel.insert(2, "Inoi")
print(tel)
# 6 listdan qiymat bo'yicha element o'chirish
tel.remove("Inoi")
print(tel)
# 7 listdan index bo'yicha element o'chirish
tel.pop(-1)
print(tel)
# 8 sonlar listini ochib unga 1 dan 10 gacha qiymat berish
number=[1,2,3,4,5,6,7,8,9,10]
# 9 sonlar listidan eng katta va eng kichik qiymatni topish
print(max(number))
print(min(number))
# 10 sonlar listidan o'rta qiymatini topish

# 11 mevalar lug'atini ochish
fruit={"Olma":5, "Olcha":5, "Nok":5, "Uzum":5}
print(fruit)
# 12 davlatlar lug'atini ochish
country={"AQSH":"Nyu-York", "Italia":"Milan", "Ispaniya":"Madrid", "Fransiya":"Parij", "Angliya":"London"}
print(country)
# 13 noutbuklar lug'atini ochish
noutbuk={"Acer":15, "Hp":15, "Asus":15, "Lenovo":15, "Dell":15}
print(noutbuk)
# 14 foydalanuvchidan yoshini so'rab uni tug'ilgan yilini ekranga chiqarish
yosh=int(input("Iltimos yoshingizni kiriting: "))
print(2024-yosh)
# 15 foydalanuvchidan 3 xonali biron-bir sonni kiritishini so'rash va bu sonni ustida 4 xil amallarni bajarish
son=int(input("Biron-bir 3 xonali son kiriting: "))
print(f"1000+{son}=>{1000+son}")
print(f"1000-{son}=>{1000-son}")
print(f"1000*{son}=>{1000*son}")
print(f"1000/{son}=>{1000/son}")
# 16 foydalanuvchidan mashina nomini kiritishini so'rash va u kiritgan moshina markasi va nomini ekranga chiqarish
mashina=input("Biron-bir mashina nomini kiriting: ")
print(f"Siz kiritgan mashina {mashina} va u chevrolet markasi ostida ishlab chiqarilgan")
# 17 foydalanuvchidan yoshini so'rab uni 100ga kirishiga nechchi yil qolganini ekranga chiqarish
ysh=int(input("Yoshingizni kiriting: "))
print(f"Sizning yoshingiz {ysh}da va siz {100-ysh} yildan so'ng 100 yoshga to'lasiz")
