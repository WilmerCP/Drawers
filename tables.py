
import csv
import os

#Yeni dosyalar olusturuyor

def newFile(path,content,callback):

    try:
        archivo = open("./drawers/"+path,'w')
    except:
        callback("Hata: "+path+" dosyasini acarken bir problem oldu")
    else:
        writer = csv.DictWriter(archivo,fieldnames=["isim","kategori","miktar"])
        writer.writeheader()

        for row in content:
            writer.writerow(row)

        archivo.close()
        callback(None)

#Boş dosyalar oluşturuyor
        
def emptyFile(path,callback):

    try:
        archivo = open("./drawers/"+path,'w')
    except:
        callback("Hata: "+path+" dosyasini acarken bir problem oldu")
    else:

        archivo.close()
        callback(None)

#Bir dosya siliyor

def deleteFile(path,callback):

    try:
        os.remove("./drawers/"+path)
    except:
        callback("Hata: "+path+" dosyasini silirken bir problem oldu")
    else:
        callback(None)

#cekmece dosyasini okuyor ve liste olarak donduruyor

def listDrawers():
    drawers = os.listdir("./drawers")
    return drawers

#bit dosyanin iceriklerini okuyor ve liste olarak gonderiyor

def readFile(path,callback):
    try:
        archivo = open("./drawers/"+path,'r')
    except:
        callback("Hata: "+path+" dosyasini acarken bir problem oldu",None)
    
    else:
        reader = csv.DictReader(archivo)

        objects = []

        for line in reader:
            objects.append(line)

        archivo.close()
        callback(None,objects)

#Yeni bir esya ekliyor

def appendContent(path,row,callback):

    try:
        archivo = open("./drawers/"+path,'a')
    except:
        callback("Hata: "+path+" dosyasini acarken bir problem oldu")
    else:
        writer = csv.DictWriter(archivo,fieldnames=["isim","kategori","miktar"])

        writer.writerow(row)

        archivo.close()
        callback(None)

#Bir esya cikariyor

def deleteElement(path,name,callback):

    try:
        archivo = open("./drawers/"+path,'r')
    except:
        callback("Hata: "+path+" dosyasini acarken bir problem oldu")
    else:
        reader = csv.DictReader(archivo)

        filtered_rows = [row for row in reader if row["isim"] != name]

        archivo.close()

        newFile(path,filtered_rows,lambda err:callback(err))


def callback(err):
    if(err is not None):
        print(err)

newFile("4.csv",[{"isim":"telefon","kategori":"samsung","miktar":"1"},
                         {"isim":"defter","kategori":"kirtasiye","miktar":"4"},
                         {"isim":"renkli kalem","kategori":"kirtasiye","miktar":"3"}],callback)

""""

deleteElement("drawers/prueba.csv","Name",callback)

def callback(err):
    if(err is not None):
        print(err)

appendContent("drawers/1.csv",{"isim":"telefon","kategori":"teknoloji","miktar":"1"},callback)

def callback(err,data):
    if(err is None and data):
        for line in data:
            print(line)
    else:
        print(err)

readFile("drawers/1.csv",callback)


newFile("drawers/2.csv",[{"isim":"kalem","kategori":"kirtasiye","miktar":"3"},
                         {"isim":"laptop","kategori":"bilgisayar","miktar":"1"},
                         {"isim":"takim karti","kategori":"ROTA","miktar":"10"}])

hola = os.listdir("./drawers")
"""