from SERCH_INFO import InfoExcel
from DES_IMAGEN import Imagenes


def menu_accion():
    print('#'*30,'MENU DE ACCION',30*'#')
    print("1. Busqueda de informacion")
    print("2. Descargar imagenes relacionada a la informacion")
    print("0. Salir")
    print('#'*30,'MENU DE ACCION',30*'#')

def main():
    while True:
        while True:
            try:
                menu_accion()
                opcion = int(input("Ingrese la opcion a realizar: "))
                if 0 <= opcion <= 3:
                    break
            except ValueError:
                print("ERROR: Debe ingresar un valor entero y que sea positivo ")
        if opcion == 0:
            break
        elif opcion == 1:
            InfoExcel()
        elif opcion == 2:
            Imagenes(url='https://www.rayados.com/fotogalerias/lista', carpeta='ImagenesRayados')


    print()
    print("El programa ha Finalizado")


if __name__ =='__main__':
    main()
    