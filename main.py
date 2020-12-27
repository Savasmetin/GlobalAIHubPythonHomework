

print(" welcome mann or womenn..")
ad="savaş"
soyad="metinoğlu"
isim= input("adınızı giriniz")
soyisim= input("soyadınızı giriniz")
true= 3
while true:
    if (ad==isim) and (soyad==soyisim):
        print("hoşgeldin"+ad)
        break
    elif (ad!=isim) and (soyad==soyisim):
        print("ismini yanlış girdin  tekrar dene")
        break
    elif (ad==isim) and (soyad!=soyisim):
        print(" soyad yanlış  tekrar dene")
        break
    else:
        print("hakkın bitti bremın")


dersler={"1:matematik","2:biyoloji","3:fizik","4:kimya","5:teknik çizim","6:yazılım"}
derssayısı=len(dersler)
bilinendersler=[]
print("Listeden en az 3 en fazla 5 ders seçmelisiniz.")
print(dersler)
count=0
while count<5:
    dersseçimi=int(input("Ders seçiminizi yapın 1-6:"))
    if dersseçimi==1:
        if("1:matematik" in bilinendersler):
            print("\n *matematik dersini zaten seçmiştiniz!!!")
            count -= 1
        else:
            bilinendersler.append[dersler(1)]
            print("\n=> {} dersi listeye eklendi!\n".format(dersler[1]))
            print(bilinendersler)
            if dersseçimi==2:
                if("2:biyoloji" in bilinendersler):
                    print("\n *biyoloji dersini zaten seçmiştiniz!!!")
                    count -=1
                else:
                    bilinendersler.append[dersler(2)]
                    print("\n=> {} dersi listeye eklendi!\n".format(dersler[2]))
                    print(bilinendersler)
                    if dersseçimi==3:
                        if("3:fizik"in bilinendersler):
                            print("\n *fizik dersini zaten seçmiştiniz!!!"),
                            count-=1
                        else:
                            bilinendersler.append[dersler(3)]
                            print("\n=> {} dersi listeye eklendi! \n".format(dersler[3]))
                            print(bilinendersler)
                            if dersseçimi==4:
                                if("4:kimya" in bilinendersler):
                                    print("\n *Kimya dersini zaten seçmiştiniz!!!")
                                    count -= 1
                                else:
                                    bilinendersler.append[dersler(4)]
                                    print("\n=> {} dersi listeye eklendi \n".format(dersler[4]))
                                    print(bilinendersler)
                                    if dersseçimi==5:
                                        if("5:teknik çizim"in bilinendersler):
                                            print("\n *teknik çizim dersini zaten seçmiştiniz!!!")
                                            count-=1
                                        else:
                                            bilinendersler.append[dersler(5)]
                                            print("\n=> {} dersi listeye eklendi \n".format(dersler[5]))
                                            print(bilinendersler)
                                            if dersseçimi==6:
                                                if("6:yazılım"in bilinendersler):
                                                    print("\n *yazılım dersini zaten seçmiştiniz!!!")
                                                    count-=1
                                                else:
                                                    bilinendersler.append[dersler(6)]
                                                    print("\n=> {} dersi listeye eklendi \n".format(dersler[6]))
                                                    print(bilinendersler)

vize = int(input('1. Yazılı : '))
final = int(input('2. Yazılı : '))
proje = int(input('3. Yazılı : '))
ortalama = float(vize * 0.3 + final * 0.5 + proje * 0.2)
print(ortalama)

if ortalama> 90:
    print("AA")

elif ortalama> 70:
    print("BB")

elif ortalama>50:
    print("CC")

elif ortalama> 30:
    print("DD")

elif 30> ortalama > 0:
    print("FF")
    print("ne kadar salak bir insansın puhh  :)")