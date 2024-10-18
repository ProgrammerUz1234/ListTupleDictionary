ism=input("Iltimos ismingizni kiriting > ")
print(f"Siznig ismingiz {ism}")




# 2
x=int(input("Yoshingizni kiriting:  "))
print(f"Siz {x} yoshdasiz")


# 

name=input("Ismingizni kiriting > ")
y=name.upper()
print(f"Sizning ismingiz {y}")




son=int(input("Tug'ilgan yilingizni kiriting: "))
y=2024
print(f"Siz {y-son} yoshdasiz")









x=int(input("Iltimos yoshingizni kiriting: "))
print(f"Siz {2024-x}-yilda tug'ilgansiz")



users={"User1":"user123", "User2":"user456", "User3":"user789"}

a=input("Useringizni kiriting > ")
b=input("User parolini kiriting > ")

print(f"User: {a.lower()}")
print(f"Password: {b.lower()}")



#1 print gap yozish
print("Mening ismim Diyor")
#2 ism list ochish 5 qiymatli 
a=['Diyor', 'Ramiz', 'Damir', 'Amir', 'Samir']
print(a)
#3 oxiridan bitta qo'shish
a.append('Mansur')
print(a)
#4 index bo'yicha qo'shish
a.insert(2, 'Sanjar')
print(a)
#5 index bo'yicha o'chirish
a.pop(2)
print(a)
#6 qiymat bo'yicha o'chirish
a.remove("Mansur")
print(a)
#7 meva lug'atini ochish qiymati=>narxi
fruit={"Olma":"5", "Uzum":"6", "Anor":"7", "Olcha":"4", "Ananas":"8"}
print(fruit)





a=int(input('Son kiriting: '))
print(f"1000-{a} = {1000-a}")
print(f"1000+{a} = {1000+a}")
print(f"1000*{a} = {1000*a}")
print(f"1000/{a} = {1000/a}")
