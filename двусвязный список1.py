class Node(object):
    def __init__(self, data, previous=None, next=None):
        self.data = data
        self.next = next
        self.previous = previous


class DoubleLink(object):
         #Двусвязный список#
    def __init__(self, data=None):
        self.head = None
        self.tail = None
        if data != None:
            self.initialization(data)

    def initialization(self, data=None):
                 #Инициализировать#
        if self.head != None:
            print("Error: Link had been initialization!")
        elif data == None:
            print("Error: Parameter data cannot be empty!")
        else:
            self._add_to_tail(data)

    def _add_to_tail(self, data):
                 #Добавить узел
        if type(data) == int:
            data = [data]
        for da in data:
            node = Node(da)
            if self.head == None:
                self.head = node
                self.tail = node
            else:
                self.tail = self.head
                while self.tail.next != None:
                    previous = self.tail
                    self.tail = self.tail.next
                    self.previous = previous
                                 # Предшественник узла node указывает на tail, а последующий указывает на tail.next
                node.previous = self.tail
                node.next = self.tail.next
                                 # Преемник хвостового узла указывает на узел, завершите добавление
                self.tail.next = node
                self.tail = self.tail.next

    def append(self, data=None):
                 #Добавить узел в конец связанного списка" ""
        self._add_to_tail(data)

    def travering(self):
                 #Распечатать все узлы
        if self.head == None:
            pass
        else:
            probe = self.head
            while probe != None:
                print(probe.data)
                probe = probe.next

    def length(self):
                 #Длина
        length = 0
        probe = self.head
        while probe != None:
            length += 1
            probe = probe.next
        return length

   
    

    def __str__(self):
        result = ""
        if self.head != None:
            probe = self.head
            while probe != None:
                result += str(probe.data) + "\n"
                probe = probe.next
        return result


