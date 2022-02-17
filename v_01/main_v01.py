from utilidad_v01 import Utilidad

def show_elementos():
    for idx, elemento in enumerate(util.elementos):
        print(" ".join([str(idx) + ".", elemento.nombre, elemento.descripcion]))


def show_postes():
    for idx, poste in enumerate(util.postes):
        print(" ".join([str(idx) + ".", poste.codigo]))

def show_all():
    print("Los elementos y sus conexiones")
    for idx, elem in enumerate(util.elementos):
        print(" ".join([str(idx) + ".", elem.nombre]))
        print("Conectado A:")
        print("-".join([e.nombre for e in elem.get_con()]))
        print('\n')
    
    print('---------------------------------------------------------------')
    print("Los postes, sus conexiones y sus elementos enganchados")
    
    for idx, poste in enumerate(util.postes):
        print(" ".join([str(idx) + ".", poste.codigo]))
        print("Enganches:")
        print("-".join([e.nombre for e in poste.enganchados]))

        print("Otros postes conectados a este:")
        print('-'.join([p.get_codigo() for p in poste.vecinos]))
        print('\n')

def menu():
    print("Seleccione la opción que desea (Digite el número)")
    print("1. Crear Poste")
    print("2. Crear Elemento")
    print("3. Enganchar elemento a poste")
    print("4. Interconectar elementos")
    print("5. Mostrar todo")
    print("6. Borrar todo.")
    print("0. Salir")

    opcion = int(input())

    if opcion == 1:
        print("Digite un codigo para el poste")
        cod = input()
        util.crear_poste(cod)
    
    elif opcion==2:
        print("Digite el nombre del elemento")
        nombre = input()
        print("Digite una breve descripcion")
        desc = input()
        util.crear_elemento(nombre, desc)

    elif opcion==3:
        print("Seleccione un elemento de la lista")
        show_elementos()
        elem = int(input())
        print("Seleccione un poste de la lista")
        show_postes()
        poste = int(input())

        try:
            print(util.elementos[elem])
            util.enganchar(elem, poste)
        
        except Exception as e:
            print(e)
            print("Operacion cancelada")


    elif opcion==4:
        print("Selecciona un elemento de la lista")
        show_elementos()
        el_1 = int(input())
        print("Seleccione otro elemento de la lista")
        el_2 = int(input())

        try:
            util.conectar(el_1, el_2)
        
        except Exception as e:
            print(e)
            print("Operación cancelada")
    
    elif opcion==5:
        show_all()

    elif opcion==6:
        util.postes.clear()
        util.elementos.clear()

    elif opcion==0:
        return False
    
    return True
    



util = Utilidad()
if __name__ == "__main__":

    while(menu()):
        pass