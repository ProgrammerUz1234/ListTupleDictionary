# Theme: Python string methods

# 1.capitalize
q="ali"
w=q.capitalize()
print(w)

# 2.casefold
e="Hello world"
r=e.casefold()
print(r)

# 3.center
t="Olcha"
y=t.center(25)
print(y)

# 4.encode
u="My name is Diyor"
i=u.encode()
print(i)

# 5.find
o="hello my name is Diyor"
p=o.find("Diyor")
print(p)

# 6.format
a="Olmaning do'kaondagi narxi {son:2000} so'm"
print(a.format(son = 5000))

# 7.index
s="diyor bugun dars o'tdi"
print(s.index("dars"))

# 8.isalnum
d="diyor123"
print(d.isalnum())

# 9.isalpha
f="ali"
print(f.isalpha())

# 10.isnumeric
g="123456789"
print(g.isnumeric())

# 11.isdigit
h="123456"
print(h.isdigit())

# 12.istitle
j="Ramiz"
print(j.istitle())

# 13.isspace
k=" "
print(k.isspace())

# 14.join
mylist=["olim", "cola"]
x=" aka ".join(mylist)
print(x)

# 15.just
l="am is 15 years old"
z=s.ljust(50)
print("I", z)

# 16.title
c="mening uyim"
print(c.title())

# 17.swapcase
v="sALOM mENING iSMIM dIYOR"
print(v.swapcase())

# 18.zfill
b="500"
print(b.zfill(5))
