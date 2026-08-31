class Node:
    def __init__(self, title, artist, year, genr):
        self.title = title
        self.artist = artist
        self.year = year
        self.genr = genr
        self.next = None

class ListaEnlazada:
    def __init__(self):
        self.head = None
        self.size = 0
        self.tail = None

    # def insert_first(self, fact):
    #     new = Node(fact)
    #     if self.head is None:
    #         self.head = new
    #         self.tail = new
    #         return
    #     new.next = self.head
    #     self.head = new
    #     self.size += 1

    def insert_end(self, title,artist, year, genr):
        new = Node(title.lower(),artist, year, genr)
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
        cont = 1
        while current is not None:
            print(f"Song {cont}. {current.title} - {current.artist} - {current.year} - {current.genr}")
            current = current.next
            cont += 1

    # def insert_at(self, fact, position):
    #     if (position == 0):
    #         self.insert_first(fact)
    #     elif (position == self.size):
    #         self.insert_last(fact)
    #     elif (position > self.size):
    #         print("The song can't be inserted")
    #     else:
    #         previous = previous.next
    #         new_mode = Node(fact)
    #         new_mode.next = previous.next
    #         previous.next = new_mode
    #         self.size += 1 


    def get_size(self):
        return self.size


    def delete_song(self, title):
        title = title.lower()
        if self.head is None:
            return None
        if self.head.title == title:
            deleted_node = self.head
            self.head = self.head.next
            
    
            if self.head is None:
                self.tail = None
                
            self.size -= 1
            return deleted_node


        current = self.head
        while current.next is not None:
            if current.next.title == title:
                deleted_node = current.next
                
                current.next = current.next.next
            
                if deleted_node == self.tail:
                    self.tail = current
                    
                self.size -= 1
                return deleted_node
            
            current = current.next
        return None

my_playlist = ListaEnlazada()

# print(my_playlist.get_size())

while True:
    print("------MENU-------")
    print("1. INSERT SONGS")
    print("2. DELETE SONGS")
    print("3. SHOW SONGS")
    print("4. EXIT")

    option = input("SELECT THE OPTION: ")

    if option == "1":
        print("-- INSERT SONG --\n")
        title = input(" INSERT SONG NAME :")
        artist = input (" INSERT ARTIST NAME :")
        year = input (" INSERT YEAR OF THE SONG :")
        genr = input (" INSERT THE GENR OF THE SONG :") 
        my_playlist.insert_end(title, artist, year, genr)
    elif option == "2":
        print("DELETE SONGS\n")
        title = input("ENTER THE NAME OF THE SONG TO DELETE : ")
        song = my_playlist.delete_song(title)
        if song:
            print(f"SONG DELETED : {song.title} - {song.artist} - {song.year} - {song.genr}")
        else:
            print("SONG NOT FOUND")
    elif option == "3":
        print("SHOW SONGS\n")
        my_playlist.print_list()
    elif option == "4":
        print("------------ PROGRAM COMPLETED delete-----------")
        break
    else:
        print("THAT ISN'T AN OPTION")
