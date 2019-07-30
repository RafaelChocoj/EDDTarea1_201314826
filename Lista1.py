
#mi clase nodo
class Nodo():
    def __init__(self , valor= None, v2 = None):
        self.valor = valor
        self.v2 = v2
        self.siguiente = None
        

    #def getValor(self):
    #    return self.valor

    #def getVal22(self):
    #    return self.v2

    #def __str__(self):
    #    return str(self.valor)

    #def __str__2(self):
    #    return str(self.v2)


#mi clselista
class Lista_enla():
   
    def __init__(self):
        self.primero = None
        self.ultimo = None

    def esVacio(self):
        if self.primero  == None:
            return True

    #para insertar nodo al principio
    def insertNodo_inicio(self, valor,v2):
    
        nuevo = Nodo(valor, v2)
        if self.esVacio() == True:    
            self.primero = nuevo
            self.ultimo = nuevo
        else:
            nuevo.siguiente  = self.primero
            self.primero = nuevo

    #para insertar nodo Al final
    def insertNodo_Final(self, valor, v2):
        
        nuevo = Nodo(valor, v2)
        
        if self.esVacio() == True:    
            self.primero = nuevo
            self.ultimo = nuevo
        else:
            self.ultimo.siguiente = nuevo
            self.ultimo = nuevo

    #eliminar primero
    def eliminar_prim(self):
        if self.esVacio()== True:
            print ("No puede eliminar primero La lista esta vacia")
        #elif self.primero == self.ultimo:
        #    self.primero = None
        #    self.ultimo = None
        #    print ("eliminado, vacio")
        else:
            aux = self.primero
            self.primero = self.primero.siguiente
            #aux = None
            aux.siguiente = None
            print ("eliminado")

    #eliminar ultimo
    def eliminar_ultimo(self):  
        if self.esVacio()== True:
            print ("No puede eliminar ultimo La lista esta vacia") 
        elif self.primero == self.ultimo:
            self.primero = None
            self.ultimo = None 
            print ("elemento ultimo eliminado, vacia")
        else:
            actual_del = self.primero
            aux22 = None
            while actual_del != None:
                if actual_del.siguiente == self.ultimo:
                    #aux22 = self.ultimo
                    #self.ultimo = actual_del
                    #aux22 = None
                    
                    aux22 = self.ultimo
                    self.ultimo = actual_del
                    actual_del.siguiente = None
                    

                    print ("elemento ultimo eliminado")
                else:
                    #aux22 = actual_del
                    actual_del = actual_del.siguiente

    #Modificando valor
    def modific_val(self, indice = None, modificado=None ):
        if self.esVacio() == True:
            print("la lista esta vacia") 

        else:
            if indice == 0:
                mod = self.primero
                mod.valor = modificado
                print ("modificado 0")
            else:
                conta = 0
                temm = self.primero
                while conta < indice:
                    temm = temm.siguiente
                    conta = conta + 1 
                temm.valor = modificado


    #Imprimir lista
    def Listar_lista(self):
        if self.esVacio()== True:
            print ("La  lista esta vacia")
        else:
            aux = self.primero
            while aux != None:
                print(aux.valor )
                #print("valor1 " + aux.valor)
                #print("valor2 " + str(aux.v2 ))
                aux = aux.siguiente
                #print(temp )
                #if temp == self.ultimo:
                #    validar = False
                #else:
                #    temp = temp.siguiente
            
if __name__ == "__main__":
    lis = Lista_enla()
    bolano = True
    while(bolano):
        print("\n\n\n")
        print("****Menu****")
        print("1.- Agregar Inicio\n"+
        "2.- Agregar Final\n"+
        "3.- Listar\n"+
        "4.- eliminar primero\n"+
        "5.- eliminar ultimo\n"+
        "7.- modificar valor\n"+
        "6.- Salir\n")
        op = input("seleccione opcion para poder continuar: ")
        if op == "1":
            val = input("Ingrese valor a ingresar al principio: ")
            #nod_add = Nodo(val,val)
            #lis.insertNodo_inicio(nod_add)
            lis.insertNodo_inicio(val, "pru1")


        elif op == "2":
            val = input("Ingrese valor a ingresar al final: ")
            #nod_add = Nodo(val,val)
            #lis.insertNodo_Final(nod_add)
            lis.insertNodo_Final(val, "val2")

        elif op == "3":
            lis.Listar_lista()
        elif op == "4":
            lis.eliminar_prim()
        elif op == "5":
            lis.eliminar_ultimo()
        elif op == "7":
            indi = int(input("Ingrese indice a modificar"))
            val = input("Ingrese nuevo valor: ")
            lis.modific_val(indi, val)
        elif op == "6":
            bolano = False