# Uy classini ochib unga kamida 4 ta xususiyat berib shu classdan meros olish va obyect bilan ekranga chiqarib berish

class Uy():
    def __init__(self, width, height, room, price):
        self.width = width
        self.height = height
        self.room = room
        self.price = price

    def get_all_uy(self):
        return self.width, self.width, self.room, self.price



class Uy1(Uy):

    def get_price(self):
        return self.price



productUy = Uy(250, 6, 5, 10000)


print(productUy.get_all_uy())


# Zavod nomli class ochib uning ichiga kamida 3 ta xususiyat berib, bu classdan ham meros olib obyect bilan ekranga chiqaring

class Zavod():
    def __init__(self, name, product, location):
        self.name = name
        self.product = product
        self.location = location

    def get_name(self):
        return self.name

    def get_product(self):
        return self.product




class Zavod1(Zavod):

    def get_location(self):
        return self.location

    def get_all_zavod(self):
        return self.name, self.product, self.location


productZavod = Zavod1("Pure Milky", "smetana", "Dagbet")
print(productZavod.get_all_zavod())


# Shahar nomli class ochib unga 5 ta xususiyat berib bu classdan ham meros olish

class Shahar():
    def __init__(self, nom, davlat, aholi, hudud, nomer):
        self.nom = nom
        self.davlat = davlat
        self.aholi = aholi
        self.hudud = hudud
        self.nomer = nomer

    def get_nom_shahar(self):
        return self.nom

    def get_davlat_shahar(self):
        return self.davlat

    def get_aholi_shahar(self):
        return self.aholi




class Shahar1(Shahar):

    def get_hudud_shahar(self):
        return self.hudud

    def get_nomer_shahar(self):
        return self.nomer

    def get_all_shahar(self):
        return self.nom, self.davlat, self.aholi, self.hudud, self.nomer



productShahar = Shahar("Samarqand", "O'zbekiston", 370000, 458, 30)
print(productShahar.get_davlat_shahar())




# Televizor classini ochib 4 xususiyat berish va shu classdan meros olish

class Televizor():
    def __init__(self, razmer, firma, smart, hdmi):
        self.razmer = razmer
        self.firma = firma
        self.smart = smart
        self.hdmi = hdmi

    def get_razmer_tel(self):
        return self.razmer

    def get_firma_tel(self):
        return self.firma



class Televizor1(Televizor):

    def get_smart_tel(self):
        return self.smart

    def get_hdmi_tel(self):
        return self.hdmi

productTelevizor = Televizor1(43, "Samsung", False, True)

print(productTelevizor.get_hdmi_tel())
