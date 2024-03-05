# Puzle Lineal con búsqueda en profundidad
#Esta version indica los movimientos (izquierda, derecha, centro) que se realizan para llegar a la solucion
from arbol import Nodo

def buscar_solucion_DFS(estado_inicial, soluciones):
    solucionado = False
    nodos_visitados = []
    nodos_frontera = []
    
    nodoInicial = Nodo(estado_inicial)
    nodos_frontera.append(nodoInicial)
    contador=0
    
    nodos_visitados.append(Nodo(nodoInicial.get_datos() +['I']))
    nodos_visitados.append(Nodo(nodoInicial.get_datos() +['C']))
    nodos_visitados.append(Nodo(nodoInicial.get_datos() +['D']))
    
    #SE AGREGARON REALIZARON PRUEBAS UTILIZANDO PRINTS PARA VERIFICAR EL FLUJO DE LOS DATOS
    # E IDENTIFICAR EL ERROR DEL CODIGO, EL CUAL SE EJECUTABA INDEFINIDAMENTE
    while (not solucionado) and len(nodos_frontera) != 0:        
        nodo = nodos_frontera.pop()
        nodoAux = nodo.get_datos()
        #print(nodo.get_datos()) 
        #print(nodoAux)
        print(nodoAux)    
        # extraer nodo y añadirlo a visitados
        #nodos_visitados.append(Nodo(nodo.get_datos() +['I']))
        #nodos_visitados.append(Nodo(nodo.get_datos() +['C']))
        #nodos_visitados.append(Nodo(nodo.get_datos() +['D']))
        nodos_visitados.append(nodo)
        
        for l in nodos_visitados:
            print("VISITADOS:",l.get_datos())
        for s in soluciones:
            if nodo.get_datos() == s:
                print("Solucion encontrada",nodo.get_datos())
                # solución encontrada
                solucionado = True
                return nodo
        
        # expandir nodos hijo
        dato_nodo = nodo.get_datos()
        
        #EL OPERADOR DERECHO SE MOVIO AQUI, PARA QUE SE EVALUE COMO ULTIMO CASO, SI ES QUE YA NO HAY HIJOS IZQUIERDOS NI CENTRALES
        # operador derecho
        hijo = [str(dato_nodo[0]), str(dato_nodo[1]), str(dato_nodo[3]), str(dato_nodo[2]),'D']
        hijo_derecho = Nodo(hijo)
        print("Hijo derecho",hijo_derecho.get_datos())
        print("Hijo en nodos visitados",hijo_derecho.en_lista(nodos_visitados))
        print("Hijo en nodos frontera",hijo_derecho.en_lista(nodos_frontera))
        if not hijo_derecho.en_lista(nodos_visitados) \
                and not hijo_derecho.en_lista(nodos_frontera):                
            nodos_frontera.append(hijo_derecho)      
        
            
        # operador central
        hijo = [str(dato_nodo[0]), str(dato_nodo[2]), str(dato_nodo[1]), str(dato_nodo[3]),'C']
        hijo_central = Nodo(hijo)
        print("Hijo central",hijo_central.get_datos())
        print("Hijo en nodos visitados",hijo_central.en_lista(nodos_visitados))
        print("Hijo en nodos frontera",hijo_central.en_lista(nodos_frontera))
        if not hijo_central.en_lista(nodos_visitados) \
                and not hijo_central.en_lista(nodos_frontera):                
            nodos_frontera.append(hijo_central)
        #SE MOVIO EL OPERADOR IZQUIERDO AQUI, PARA QUE SE EVALUE PRIMERO EN LA SIGUIENTE ITERACION, Y ASI FUNCIONE COMO EL ALGORITMO DFS, 
        # QUE EVALUA PRIMERO EL HIJO IZQUIERDO
        # operador izquierdo
        hijo = [str(dato_nodo[1]), str(dato_nodo[0]), str(dato_nodo[2]), str(dato_nodo[3]),'I']
        hijo_izquierdo = Nodo(hijo)
        print("Hijo izquierdo",hijo_izquierdo.get_datos())
        print("Hijo en nodos visitados",hijo_izquierdo.en_lista(nodos_visitados))
        print("Hijo en nodos frontera",hijo_izquierdo.en_lista(nodos_frontera))
        if not hijo_izquierdo.en_lista(nodos_visitados) \
                and not hijo_izquierdo.en_lista(nodos_frontera):                
            nodos_frontera.append(hijo_izquierdo)
        nodo.set_hijos([hijo_izquierdo, hijo_central, hijo_derecho]) 
        contador+=1



if __name__ == "__main__":
    estado_inicial=['4','2','3','1']
    solucion=[['1','2','3','4','I'],['1','2','3','4','C'],['1','2','3','4','D']]
    nodo_solucion = buscar_solucion_DFS(estado_inicial, solucion)
    # mostrar resultado
    resultado=[]
    nodo=nodo_solucion
    while nodo.get_padre() != None:
        resultado.append(nodo.get_datos())
        nodo = nodo.get_padre()

    resultado.append(estado_inicial)
    resultado.reverse()
    print("Estado Inicial: ",estado_inicial)
    print("Estadi objetivo: ",solucion)
    print("Solucion: ",resultado)