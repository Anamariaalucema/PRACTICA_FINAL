class NodoBinario:
    def __init__(self, valor):
        self.valor = valor
        self.padre = None
        self.hijo_izquierdo = None
        self.hijo_derecho = None

def recorrido_arbol_en_orden_iterativo(raiz, callback):
    pila = []
    nodo_actual = raiz

    while True:
        if nodo_actual is not None:
            pila.append(nodo_actual)
            nodo_actual = nodo_actual.hijo_izquierdo
        elif pila:
            nodo_actual = pila.pop()
            callback(nodo_actual)
            nodo_actual = nodo_actual.hijo_derecho
        else:
            break

def imprimir_valor_nodo(nodo):
    print(nodo.valor)

# Crear el árbol binario de ejemplo
nodo_1 = NodoBinario(1)
nodo_2 = NodoBinario(2)
nodo_3 = NodoBinario(3)
nodo_4 = NodoBinario(4)
nodo_5 = NodoBinario(6)
nodo_6 = NodoBinario(7)
nodo_7 = NodoBinario(9)

nodo_1.hijo_izquierdo = nodo_2
nodo_1.hijo_derecho = nodo_3
nodo_2.padre = nodo_1
nodo_3.padre = nodo_1

nodo_2.hijo_izquierdo = nodo_4
nodo_2.hijo_derecho = nodo_5
nodo_4.padre = nodo_2
nodo_5.padre = nodo_2

nodo_3.hijo_derecho = nodo_6
nodo_6.padre = nodo_3

nodo_4.hijo_derecho = nodo_7
nodo_7.padre = nodo_4

# Llamar a la función de recorrido en orden
recorrido_arbol_en_orden_iterativo(nodo_1, imprimir_valor_nodo)
