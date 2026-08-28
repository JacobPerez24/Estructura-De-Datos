class Node:
    def __init__(self, fact):
        self.fact = fact
        self.next = None

class ListaEnlazada:
    def __init__(self):
        self.head = None
        self.size = 0
        self.tail = None

    def insert_first(self, fact):
        new = Node(fact)
        if self.head is None:
            self.head = new
            self.tail = new
            return
        new.next = self.head
        self.head = new
        self.size += 1

    def insert_end(self, fact):
        new = Node(fact)
        if self.head is None:
            self.head = new
            self.tail = new
            return
        current = self.head
        while current.next is not None:
            current = current.next
        current.next = new
        self.size += 1

    def print_list(self):
        current = self.head
        while current is not None:
            print(f"Fact: {current.fact}  Address: {(current)}")
            current = current.next

    def insert_at(self, fact, position):
        if (position == 0):
            self.insert_first(fact)
        elif (position == self.size):
            self.insert_last(fact)
        elif (position > self.size):
            print("The data can't be inserted")
        else:
            previous = previous.next
            new_mode = Node(fact)
            new_mode.next = previous.next
            previous.next = new_mode
            self.size += 1 


    def get_size(self):
        return self.size

my_list = ListaEnlazada()
my_list.insert_first(42)

print(f"Cabeza de la lista: {my_list.head}")
my_list.insert_end(26)
my_list.print_list()
print(my_list.get_size())



#         # insert_first
#         # insert_last
#         # insert_at
#         # print_list
#         # get_size

# #definir los metodos de la clase ListaEnlazada

# n1 = Node(42)
# n2 = Node(26)
# n3 = Node(10)

# n1.next = n2
# n2.next = n3

# actual = n1
# cont = 1 

# while actual is not None:
#     print(f"Nodo{cont} Dato: {actual.fact}  Direccion: {id(actual)}")
#     cont += 1
#     actual = actual.next


# print(n1.fact)       
# print(n1.next)  

        


    