class Nodo:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def insertar(raiz, key):
    if raiz is None:
        raiz = Nodo(key)

    elif key < raiz.key:
        if raiz.left is None:
            raiz.left = Nodo(key)
        else:
            raiz.left = insertar(raiz.left, key)

    elif key > raiz.key:
        if raiz.right is None:
            raiz.right = Nodo(key)
        else:
            raiz.right = insertar(raiz.right, key)

    return raiz

def busqueda(raiz, codigo):
    if raiz is None:
        print("el número no se encuentra")
    elif raiz.key == codigo:
        print("el número se encuentra")
    elif codigo < raiz.key:
        busqueda(raiz.left, codigo)
    elif codigo > raiz.key:
        busqueda(raiz.right, codigo)

def preorden(raiz):
    if raiz:
        print(raiz.key, end=" ")
        preorden(raiz.left)
        preorden(raiz.right)

def inorden(raiz):
    if raiz:
        inorden(raiz.left)
        print(raiz.key, end=" ")
        inorden(raiz.right)

def postorden(raiz):
    if raiz:
        postorden(raiz.left)
        postorden(raiz.right)
        print(raiz.key, end=" ")


def main():
    codigos = [50, 30, 70, 20, 40, 60, 80]
    raiz = None
    for key in codigos: 
        raiz = insertar(raiz, key)

    busqueda(raiz, 60)
    busqueda(raiz, 25)
    busqueda(raiz, 80)

    print("\n\\Preorden: ")
    preorden(raiz)
    print("\n\\Inorden: ")
    inorden(raiz)
    print("\n\\Postorden: ")
    postorden(raiz)

    parte4 = [25, 65, 90]
    for key in parte4: 
        raiz = insertar(raiz, key)
    print("\n\\Postorden: ")
    postorden(raiz)

    parte5 = [10, 20, 30, 40, 50]
    raiz2 = None
    for key in parte5: 
        raiz2 = insertar(raiz2, key)

    parte6 = [10, 20, 30]
    raiz3 = None
    for key in parte6: 
        raiz3 = insertar(raiz3, key)

main()