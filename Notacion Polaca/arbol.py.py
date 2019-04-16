class Nodo():
    def __init__(self, val, izq=None, der=None):
        self.valor = val
        self.izq = izq
        self.der = der

        
    def postorden(arbol):
        if arbol != None:
            postorden(arbol.obtenerHijoIzquierdo())
            postorden(arbol.obtenerHijoDerecho())
            print(arbol.valor)

    def obtenerHijoIzquierdo():
        return self.izq

    def obtenerHijoIzquierdo():
        return self.der
