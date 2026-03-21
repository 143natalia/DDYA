class Nodo:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def preorden(actual):
    if actual is None:
        return []
    return [actual.key] + preorden(actual.left) + preorden(actual.right)

def insertar(raiz, key, accion, k):
    if raiz is None:
        if key == "A":
            print("no hay pacientes")
            return None
        return Nodo(0)

    if key == "C":
        print(f"Paciente C nuevo: {accion}")
        if raiz.left is None:
            raiz.left = Nodo(accion)
        else:
            raiz.left = insertar(raiz.left, key, accion, k)
        

    elif key == "N":
        print(f"Paciente N nuevo: {accion}")
        if raiz.right is None:
            raiz.right = Nodo(accion)
        else:
            raiz.right = insertar(raiz.right, key, accion, k)

    elif key == "A":
        atender = preorden(raiz)
        if k <= len(atender):
            print(f"Atendiendo a paciente: {atender[k-1]}")

    return raiz

def main():
    acciones = int(input("cuantas acciones va a realizar: "))
    raiz = None 
    k = 1
    
    for i in range(acciones):
        indicacion = input(f"Acción {i+1}: ").split()
        key = indicacion[0]
        if key == "A":
            accion = 0
            raiz = insertar(raiz, key, accion, k)
            k += 1
        else:
            accion = indicacion[1]
            raiz = insertar(raiz, key, accion, k)
main()