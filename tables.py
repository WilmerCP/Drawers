
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

#bir dosyanin iceriklerini okuyor ve liste olarak gonderiyor

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
