import math

class Haromszog:
    def __init__(self,a,b,c):
        self.a = float (a) 
        self.b = float (b)
        self.c = float (c)

    def Kerulet(self):
        return self.a + self.b + self.c

    def Terulet(self):
        s = self.Kerulet() / 2
        return (s * (s-self.a) * (s-self.b) * s-self.c )**(1/2)
    
    def MagassagA(self):
        return 2 * self.Terulet() / self.a
    
    def MagassagB(self):
        return 2 * self.Terulet() / self.b

    def MagassagC(self):
        return 2 * self.Terulet() / self.c

    def Alfa(self):
        return math.degrees(math.acos((self.b**2 + self.c**2 - self.a**2)/(2*self.b*self.c)))

    def Betta(self):
        return math.degrees(math.acos((self.a**2 + self.c**2 - self.a**2)/(2*self.a*self.c)))

    def Gamma(self):
        return math.degrees(math.acos((self.a**2 + self.b**2 - self.c**2)/(2*self.a*self.b)))
#0 
print("Háromszögek feldolgozása 'class' segítségével.")

#1
a = input("a = ").replace(',','.')
b = input("b = ").replace(',','.')
c = input("c = ").replace(',','.')

har1 = Haromszog(a,b,c)
har2 = Haromszog(10,10,10)
har3 = Haromszog('15','15','15')

adatsor = "20;20;20"
har4 = Haromszog(*(adatsor.split(';')))
#A split az adatsort részekre bontja és elhelyezi egy szöveges tupleban.
#Csillag operátor a tuplet felosztja és hozzárendeli a megfelelő paraméterekhez.


#3
print(f"K = {har1.Kerulet():.2f}")
print(f"K = {har2.Kerulet():.2f}")
print(f"K = {har3.Kerulet():.2f}")
print(f"K = {har4.Kerulet():.2f}")
print()

print(f"T={har1.Terulet():.2f}")
print(f"ma={har2.MagassagA():.2f}")
print(f"mb={har3.MagassagB():.2f}")
print(f"mc={har4.MagassagC():.2f}")