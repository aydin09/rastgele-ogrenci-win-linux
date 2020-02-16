import random
from tkinter import *

ogr=[]

def ekle():
    dosya = open("sinif.txt",mode="r",encoding="utf-8")

    if ogr==[]:
        for i in dosya.readlines():
            ogr.append(i)
    else:       
        yazi.config(text="Kayıtlı Öğrenci Zaten Eklemişsiniz!\n")
    
def degistir():
    if ogr ==[]:
        yazi.config(text="Kayıtlı öğrenci kalmadı!\nÖğrenci Ekleden sonra Öğrenci Seç butonuna tekrar basınız.")

    else:   
        rast=random.choice(ogr)
        
        yazi.config(text=rast)

        ogr.remove(rast)
 
pencere=Tk()
pencere.geometry("400x100")
baslik = pencere.title("Öğrenci Seçim Programı")

yazi=Label(pencere,text="Öğrenci isimleri buraya gelecek\nÖğrenci Ekle butonuna ardından Öğrenci Seç butonuna basınız.")
yazi.pack()

dugme=Button(pencere,text="Öğrenci Seç",command=degistir)
dugme.pack()

dugme1=Button(pencere,text="Öğrenci Ekle",command=ekle)
dugme1.pack()

pencere.mainloop()

