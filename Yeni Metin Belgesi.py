string="ad","soyad"
ad=input("adınız:")
soyad=input("soyadınız:")
dgm=int(input("dogum yılınız:"))
yas = 2020 -  dgm
print(yas)
list1=(ad,soyad,dgm,yas)
print(list1)
if  0< yas<18:

   print(" yasak var çıkma")

else:
   print("dışarı çıkabilirsin ")