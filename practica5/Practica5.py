import requests
from bs4 import BeautifulSoup
import os


def Imagenes(url, carpeta):
    try:
        os.mkdir(os.path.join(os.getcwd(), carpeta))
        print("Carpeta creada")
    except:
        pass
        print("Carpeta creada con anterioridad, imagenes guardadas")
    os.chdir(os.path.join(os.getcwd(), carpeta))

    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    #imagen = soup.find_all("span",{"class":"img"},limit=10)
    imagen= soup.find_all('img')[11:20]
    cont =1
    for image in imagen:
        NombreImagen = "img" + str(cont) + ".jpg"
        link = image['src']
        cont +=1
        with open(NombreImagen, 'wb') as f:
            im = requests.get(link)
            f.write(im.content)
            print('Guardando Imagen: ',NombreImagen)
            
#Se crea una carpeta con las imagenes conseguidas 
Imagenes(url='https://www.rayados.com/fotogalerias/lista', carpeta='ImagenesRayados')
