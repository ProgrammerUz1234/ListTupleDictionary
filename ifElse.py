# 1 foydalanuvchidan yoshini so'rang agar u 16 va undan katta bo'lsaekranda sizga kirish mumkin aks holda ekranda sizga kirish mumkin emas degan ogohlantirish paydo bo'lsin
a=int(input("Yoshingizni kiriting> "))
if a>=16:
    print("Siz sytga kirishingiz mumkin")
else:
    print("Siz saytga kirishingiz mumkin emas! ")

# 2 foydalanuvchidan uning bo'yini so'rang agar uning bo'yi 160cm dan uzun bo'lsa yoki 160cm bo'lsa ekranda sizga atraksionda uchishingiz mumkin aks holda sizning atraksionga kirishingiz mumkin emas degan yozuv chiqsin
b=int(input("Bo'yingizni kiriting(cm)> "))
if b>=160:
    print("Siz atraksionga kirishingiz mumkin! ")
elif b<160:
    print("Siz atraksionga kirishingiz mumkin emas! ")
else:
    print("Iltimos bo'yingizni faqat cm larda kiriting! ")

# 3 foydalanuvchidan qaysi ishda ishlashini so'rang va agar u ham dasturchi bo'lsa ekranda men ham shu ishda ishlayman degan yozuv chiqsin
c=input("Ishlaydigan ishingizni kiriting> ")
if c.lower()=="dasturchi":
    print("Men ham shu ishda ishlayman! ")
elif c.lower()=="dizayner":
    print("Men ham shu yo'nalish bo'yicha ishlayman! ")
elif c.lower()=="marketolog":
    print("Men ham shu yo'nalishda ishlayman! ")
elif c.lower()=="targetolog":
    print("Men ham shu yo'nalishda ishlayman! ")
else:
    print(f"Men dasturchiman lekin, {c} ham yaxshi ish! ")
    
# 4 foydalanuvchidan uning yilini so'rang va u agar 2004 yoki undan katta bo'lsa Siz institutga kirdingiz degan yozuv chiqsin aks holda siz institutga kira olmadingiz degan yozuv chiqsin!
d=int(input("Tug'ilgan yilingizni kiriting> "))
if d<=2004:
    print("Siz institutga qabul qilindingiz! ")
else:
    print("Afsuski, Siz institutimizga qabul qilinmadingiz. Keyingi yil albatta harakat qilib ko'ring! ")

# 5 foydalanuvchidan uning ismini so'rang va agar uning ismining bosh harfi M bilan boshlansa qalaysan do'stim degan xabar chiqsin
e=input("Ismingizni kiriting> ")
if e[0]=="M":
    print("Qalaysan do'stim! ")
else:
    print("Uzur sizni tanimadim! ")
