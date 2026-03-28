
def inicializa_datos(bodegas, rutas):
    ing_bodegas = input("Ingrese el nombre de las bodegas, separadas por comas (1,2,a,r,66): ")
    lista_bodegas = [b.strip() for b in ing_bodegas.split(",")]
    for b in lista_bodegas:
        bodegas[b] = []
    
    num_rutas = int(input("Ingrese en número de rutas entre bodegas: "))
    i = 1
    print("Ingrese la conecciones entre dos bodegas, formato A B, 1 2, 67 69")
    while i <= num_rutas:
        ruta = ()
        rut = input(f"Ruta {i}: ")
        origen, destino = rut.split(" ")
        ruta = (origen, destino)
        rutas.append(ruta)
        i += 1

    for origen, destino in rutas:
        if origen != destino:  
            if destino not in bodegas[origen]:
                bodegas[origen].append(destino)
            if origen not in bodegas[destino]:
                bodegas[destino].append(origen)

    return bodegas, rutas

def modificar_grafo(bodegas, rutas):
    nuevos = input("Ingrese nueva(s) bodega(s) (separados por comas): ")
    nuevos_b = [b.strip() for b in nuevos.split(",")]
    for b in nuevos_b:
        if b not in bodegas:
            bodegas[b] = []
        else:
            print(f"El vértice {b} ya existe")

    
    nuevas_r = int(input("Ingrese en número de nuevas rutas entre bodegas: "))
    i = 1
    print("\nIngrese nuevas rutas (ej: A B): ")
    while i <= nuevas_r:
        r = ()
        rut = input(f"Ruta {i}: ")
        origen, destino = rut.split(" ")
        r = (origen, destino)
        rutas.append(r)
        i += 1
    for origen, destino in rutas:
        if origen != destino:  
            if destino not in bodegas[origen]:
                bodegas[origen].append(destino)
            if origen not in bodegas[destino]:
                bodegas[destino].append(origen)
    return bodegas, rutas

def agregar_arista(bodegas, u, v):
    if u == v:
        bodegas[u].append(v)
    if u not in bodegas[v]:
        bodegas[v].append(u)
    if v not in bodegas[u]:
        bodegas[u].append(v)
        

def lista_adjacencia(aristas, bodegas):
    for u, v in aristas:
        agregar_arista(bodegas, u, v)

    for v in bodegas:
        bodegas[v] = sorted(bodegas[v])

    print("Lista de adyacencia:")
    for v in bodegas:
        print(f"{v}: {bodegas[v]}")


def bfs(bodegas, inicio):
    visitados = []  
    cola = [] 
    cola.append(inicio)
    visitados.append(inicio) 

    while cola:
        nodo = cola.pop(0)
        print(nodo)

        for vecino in bodegas[nodo]:
            if vecino not in visitados:
                visitados.append(vecino)
                cola.append(vecino)
    return visitados

def recorrido_dfs(bodegas, nodo, visitados):
    print(nodo)
    for vecino in bodegas[nodo]:
        if vecino not in visitados:
            visitados.append(vecino)
            recorrido_dfs(bodegas, vecino, visitados)
    return visitados

def comparacion(bodegas, inicio, llegada):
    visitados = []
    visitados.append(inicio)
    recorrido_bfs = bfs(bodegas, inicio)
    dfs= recorrido_dfs(bodegas, inicio, visitados)
    print(f"recorricod con dfs: {dfs}")
    print(f"recorricod con bfs: {recorrido_bfs}")
    pos1 = 0
    pos2 = 0
    total = len(dfs)
    for i in range(total):
        if dfs[i] == llegada:
            pos1 = i
        if recorrido_bfs == llegada:
            pos2 = i
    if pos1 < pos2:
        print(f"La mejor opción para llegar a {llegada} desde {inicio} es seguir el recorrido DFS")
    else:
        print(f"La mejor opción para llegar a {llegada} desde {inicio} es seguir el recorrido BFS")

def menu(bodegas, rutas):
    print("\nMENÚ\n\n1) Imprimir lista de adjacencia\n2) Mostrar recorrido de todas las bodegas estilo BFS\n3) Mostrar recorrido de todas las bodegas estilo DFS\n4) Comparar los recorridos BFS y DFS y recomendar el mejor\n5) Agregar nuevas bodegas y rutas\n6) Terminar programa")
    opcion = int(input("Escoga la opción que desea ejecutar: "))


    if opcion == 1:
        lista_adjacencia(rutas, bodegas)
        menu(bodegas, rutas)
    if opcion == 2:
        inicio = input("¿Por cúal bodega empezar el recorrido?: ")
        recorrido_bfs = bfs(bodegas, inicio)
        print(f"recorrido con bfs: {recorrido_bfs}")
        menu(bodegas, rutas)
    if opcion == 3:
        inicio = input("¿Por cúal bodega empezar el recorrido?: ")
        visitados = []
        visitados.append(inicio)
        dfs= recorrido_dfs(bodegas, inicio, visitados)
        print(f"recorrido con dfs: {dfs}")
        menu(bodegas, rutas)
    if opcion == 4:
        inicio = input("¿Por cúal bodega empezar el recorrido?: ")
        llegada = input("¿A cúal bodega desea llegar?: ")
        comparacion(bodegas, inicio, llegada)
        menu(bodegas, rutas)
    if opcion == 5:
        bodegas, rutas = modificar_grafo(bodegas, rutas)
        menu(bodegas, rutas)
    if opcion == 6:
        print("Programa finalizado")
        exit()


def main():
    print("WAZE PARA TUS VIAJES ENTRE BODEGAS")
    print("Para iniciar el programa, se necesita la información de tus bodegas y las rutas entre ellas")

    bodegas = {}
    rutas = []
    bodegas, rutas = inicializa_datos(bodegas, rutas)
    menu(bodegas, rutas)

main()