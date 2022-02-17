
class Utilidad:
    def __init__(self):
        self.postes = []
        self.elementos = []
    def enganchar(self, id_elem, id_poste):
        elemento = self.elementos[id_elem]
        poste = self.postes[id_poste]

        elemento.enganchar(poste)
        poste.enganchar(elemento)

    def conectar(self, id_el1, id_el2):
        elemento_1 = self.elementos[id_el1]
        elemento_2 = self.elementos[id_el2]

        elemento_1.conectar(elemento_2)
        elemento_2.conectar(elemento_1)

    def crear_poste(self, codigo, max_con=8, idx = None):
        if idx != None:
            self.postes.insert(idx, Poste(codigo, max_con=max_con))
        else:
            self.postes.append(Poste(codigo, max_con=max_con))

    
    def crear_elemento(self, nombre, desc, idx = None):
        if idx != None:
            self.elementos.insert(idx, Elemento(nombre, desc))
        else:
            self.elementos.append(Elemento(nombre, desc))

class Enganchable:
    poste = None

    def enganchar(self, poste):
        if self.poste == None and type(poste) == Poste:
            self.poste = poste
        else:
            raise Exception("Unable to 'enganchar'")
    
    def get_poste(self):
        return self.poste

class Interconectable:
    conexiones = []
    def conectar(self, otro):
        pass
            
    def get_con(self):
        return self.conexiones

class Elemento(Enganchable, Interconectable):
    def __init__(self, nombre, descripcion):
        self.nombre = nombre
        self.descripcion = descripcion

    def conectar(self, otro):
        if not(otro in self.conexiones) and self != otro:
            self.conexiones.append(otro)
        else:
            raise("Failed to connect.")

class Poste:
    def __init__(self, codigo, max_con=8):
        self.enganchados = []
        self.n_con = 0  # Numero de conexiones actuales al poste
        self.MAX_CON = max_con    # Numero maximo de conexiones
        self.codigo = codigo
        self.vecinos = []

    def get_codigo(self):
        return self.codigo
        
    def enganchar(self, elemento:Enganchable):
        if self.n_con < self.MAX_CON and elemento.get_poste != None:
            
            # Agrega el poste a la lista de vecinos
            if not(elemento.get_poste() in self.vecinos):
                self.vecinos.append(elemento.get_poste())

            # Engancha el elemento
            self.enganchados.append(elemento)
            self.n_con+=1
        else:
            # Elimina el vecino agregado
            self.vecinos.pop()
            raise Exception("Maximun number of 'enganches' reached.")
            