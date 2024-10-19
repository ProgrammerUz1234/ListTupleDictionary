# python dasturlash tilida for sikl operatori

s=[1,2,3,4,5,6,7,8,9]
for son in s:
    print(son)

# pass

s=[1,2,3,4,5,6,7,8,9]
for son in s:
    if son==7:
        pass
    else:
        print(son)

# continue

s=[1,2,3,4,5,6,7,8,9]
for y in s:
    if y==6:
        continue
    else:
        print(y)

# break
s=[1,2,3,4,5,6,7,8,9]
for num in s:
    if num==5:
        break
    else:
        print(num)


avto=["Nexia2", "telefon", "Jentra", "olma", "Cobalt", "Damas", 1, 2]
for a in avto:
    if a=="telefon":
        continue
    elif a=="olma":
        continue
    elif a==1:
        continue
    elif a==2:
        continue
    else:
        print(a)




num=[12,1515,541521,45152,5152102,54521320,56152102,5641512,5646541321,12153,54513,123]
for i in num:
    if i==12:
        pass
    elif i==1515:
        pass
    elif i==45152:
        pass
    elif i==12153:
        pass
    else:
        print(i)



oila=["otam","onam","opam","akam","men","singlim","ukam","xolam","tog'am","ammam"]
for i in oila:
    if i=="xolam":
        pass
    elif i=="tog'am":
        pass
    elif i=="ammam":
        pass
    else:
        print(i)


b=[1,2,3,4,5,6,7,8]
for i in b:
    if i==8:
        break
    else:
        print(i)
        
        
        
        
s=[0,20,40,60,80,100,120,140,160,180,200,220,240,260,280,300]
for a in s:
    if a==240:
        break
    else:
        print(a)



dost=["ali","vali","eshmat","toshmat"]
for d in dost:
    print(f"Salom do'stim {d}")


# 1 bitta list ochib uning ichiga mashinalar nomini yozish
car=["Nexia2", "Cobalt", "Gentra", "Malibu", "Li9"]

# 2 for orqali foydalanuvchiga bu eng yaxshi mashinalar ro'yxati ekanligini aytish
for c in car:
    print(f"Eng yaxshi mashina: {c}")

# 3 biror list ochib unga sonlar qiymatini berish va ulardan 3xonali va undan kattalarini ekranga chiqarish
num=[123,12,1123,456,5415,541651,4561,1561,45,5454,545]
for n in num:
    if n<999 or n>99:
        print(n)
    else:
        print()
        
# 4 list ochib uning ichiga int va strlardan ma'lumot qo'yish va for yordamida faqat sonlarni ekranga chiqarish
numstr=[1,2,3,"hello",5,6,8,"salom", 11,45,48]
for s in numstr:
    if s=="hello":
        pass
    elif s=="salom":
        pass
    else:
        print(s)

# 5 foydalanuvchidan yoshini so'rang
ism=int(input("Yoshingizni kiriting> "))
a=[]
if ism>=16:
    a.append(ism)
    print("Siz saytga kirishingiz mumkin! ")
    print(a)
else:
    print("Siz saytga kirishingiz mumkin emas! ")
