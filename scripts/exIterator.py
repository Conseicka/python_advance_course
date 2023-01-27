#Los iteradores son estructuras de datos que guardan datos infinitos
#Los iterables son estructuras dedatos divisibles en elementos unicos que se pueden recorrer en un ciclo
#Protocolo de los iteradores: Es una clase con 2 metodos importantes, iter y next
#Los iteradores ahorran memoria
class EvenNumbers:
    #Clase que implementa un iterador de todos los umeros pares, o los numeros pares hasta un maximo

    def __init__(self. max = None):
        self.max = max

    def __iter__(self):
        #Aqui se tienen los elementos y atributos para que el iterador funcione
        #Aqui se convierte un iterable en un iterador
        self.num = 0
        return self

    def __next__(self):
        #Este metodo permite extraer todos los elementos en de un iterador
        if not self.max or self.num <= self.max:
            result = self.num
            self.num += 2
            return result
        else:
            raise StopIteration




def exampleIterator_1():
#creando un iterador
    my_list = [1, 2, 3, 4, 5]
    my_iter = iter(my_list)

    #iterando un iterador

    print(next(my_iter))

#Cuando no quedan datos, la excepcio StopIteration es elevada
def exampleFor():
    my_list = [1, 2, 3, 4, 5]
    my_iter = iter(my_list)

    #iterando un iterador
    while True:
        try:
            element = next(my_iter)
            print(element)
        except StopIteration:
            break

if __name__ == '__main__':
    #exampleIterator_1()
    exampleFor()
