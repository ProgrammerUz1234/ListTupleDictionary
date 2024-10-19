# while 

son=int(input("Son kiriting> "))
ishora=True

while ishora:
    if son>=10:
        print(son)
        break
    else:
        print("Iltimos 10 dan kichik son kiritmang! ")
        break


# savol
savol="Iltimos son kiriting \n"
savol+="To'xtatish uchun (exit)> "
x=True


while x:
    qiymat=input(savol)
    if qiymat=="exit":
        x=False
    else:
        qiymat=int(qiymat)
        print(f"{qiymat} ning kvadrati {qiymat**2}")


son=("Iltimos son kiriting va soningizga 100 qo'shamiz \n\n")
son+=("To'xtatish uchun (stop)> ")


while True:
    x=input(son)
    if x=="stop":
        break
    else:
        x=int(x)
        print(f" {x} ni 100 ga qo'shsak {100+x}")
















son=("Iltimos son kiriting \n\n")
son+=("To'xtatish uchun (s)> ")
t=True

while t:
    x=input(son)
    if x=="s":
        t=False
    else:
        x=int(x)
        print(f"{x}ni 10ga qo'shsak {x+10}")
        print(f"{x}ni 10ga ko'paytirsak {x*10}")
        print(f"{x}ni 10ga bo'lsak {x/10}")
        print(f"{x}dan 10ni ayirsak {x-10}")










ism=("Ismingizni kiriting /n/n")
ism+=("To'xtatish uchun (stop)> ")
t=True


while t:
    x=input(ism)
    if x=="stop":
        t=True
    else:
        print(f"{x}123")
