from arbol import *
from pila import *

def notacionPI(lista,pila):
    if lista!=[] :
        print "Entreee con:"+lista+"ASDAS"
        if lista[0]!="+" or lista[0]!="-" or lista[0]!="*" or lista[0]!="/":
            pila.apilar(Nodo(lista[0]))
        else:
            der = pila.desapilar()
            izq = pila.desapilar()
            pila.apilar(Nodo(lista[0],izq,der))  
        return notacionPI(lista[1:],pila) 
def resultado(arbol):
    if arbol.valor=="+":
        return resultado(arbol.izq) + resultado(arbol.der)
    if arbol.valor=="-":
        return resultado(arbol.izq) - resultado(arbol.der)
    if arbol.valor=="*":
        return resultado(arbol.izq) * resultado(arbol.der)
    if arbol.valor=="/":
        return resultado(arbol.izq) / resultado(arbol.der)
    return arbol.valor

pila=Pila()
ejercicio1=open('operaciones.txt','r').read().split('\n')
notacionPI(ejercicio1,pila)
print resultado(pila.desapilar())

