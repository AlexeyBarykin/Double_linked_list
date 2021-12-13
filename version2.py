import functools
import time

def slow_down(func):
    #Подождать секунду перед тем как вызывать функцию 
    @functools.wraps(func)
    def wrapper_slow_down(*args, **kwargs):
        time.sleep(1)
        return func(*args, **kwargs)
    return wrapper_slow_down



@slow_down
def countdown(from_number):
    if from_number < 1:
        print("Liftoff!")
    else:
        print(from_number)
        countdown(from_number - 1)

class Node(object):
    def __init__(self, data, index = 0, previous=None, next=None):
        self.data = data
        self.next = next
        self.previous = previous
        self.index = index

    def get_data(self):
        return self.data

    def get_previous(self):
        return self.previous

    def get_next(self):
        return self.next

    def get_index(self):
        return self.index 


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

    def __iter__(self):
        self.__curr = self.head
        return self

    def __next__(self):
        if self.__curr is None:
            raise StopIteration()
        dat = self.__curr.get_data()
        ind = self.__curr.get_index()
        self.__curr = self.__curr.get_next()
        return ind, dat

    def _add_to_tail(self, data):
                 #Добавить узел
        if type(data) == int:
            data = [data]
        for da in data:
            node = Node(da)
            if self.head == None:
                self.head = node
                self.tail = node
                node.index = 0
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
                tmp1 = node.get_index()
                node.index = tmp1+1

                self.tail.next = node
                self.tail = self.tail.next

    def find_index(self, data):    #найти индекс узла по значению
        node = self.head
        for i in range(self.tail.index + 1):
            if data != node.data:
                node = node.next
            else:
                return node.get_index()
        return 'Not on the list'

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


lst1 = DoubleLink()
lst1.__init__()

f = open('file1.txt', 'r')
for lines in f.readlines():
    lst1._add_to_tail(lines)


print(lst1.find_index(100))

lst1.travering()
lst1.__iter__()
for i in range(5):
    print(lst1.__next__())

