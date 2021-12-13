import functools
import time
import pickle

def slow_down(func):
    #Подождать секунду перед тем как вызывать функцию 
    @functools.wraps(func)
    def wrapper_slow_down(*args, **kwargs):
        time.sleep(5)
        return func(*args, **kwargs)
    return wrapper_slow_down



@slow_down
def countdown(from_number):
    if from_number < 1:
        print("начинаем")
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

    def values(self):
        node = self.head
        while node:
            yield node.data
            node = node.next

    @slow_down
    def display_values(self):  # вывести значения
        for x in self.values():
            print(x, end =' ')

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

    def find_value(self, index):   #найти значение узла по индексу
        if index > self.tail.index:
            print("Index out of range")
        else:
            node = self.head
            for i in range(index):
               node = node.next
            return node.get_data()

    #добавляем узел в конец списка
    def _add_to_tail(self, data):
                 #Добавить узел
        node = Node(data)
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
                    tmp1 = node.get_index()
                    node.index = tmp1+1
                                 # Предшественник узла node указывает на tail, а последующий указывает на tail.next
                node.previous = self.tail
                node.next = self.tail.next
                                 # Преемник хвостового узла указывает на узел, завершите добавление

                self.tail.next = node
                self.tail = self.tail.next
                self.tail.index +=1

    def find_index(self, data):    #найти индекс узла по значению
        node = self.head
        for i in range(self.tail.index + 1):
            if data != node.data:
                node = node.next
            else:
                return node.get_index()
        return 'Not on the list'

    def append(self, data=None):
                 #Добавить узел в конец связанного списка
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
                 #Длина списка
        length = 0
        probe = self.head
        while probe != None:
            length += 1
            probe = probe.next
        return length

    def delete_node(self, indx):   # удаление по индексу
        tmp2 = self.tail.index
        if indx > self.tail.index:
            print("Index out of range")
        elif indx == self.tail.index:
            node = self.head
            for i in range(indx - 1):
                node = node.next
            node.next = None
            self.tail = node
        elif indx == 0:
            tmp = self.head.next.next
            self.head = self.head.next
            self.head.next = tmp
            node = self.head
            for i in range(indx, self.tail.index):
                node.index -= 1
                node = node.next

        else:
            node = self.head
            for i in range(indx-1):
                node = node.next
            node.next = node.next.next
            for i in range(indx, self.tail.index):
                node = node.next
                node.index -= 1
            self.tail = node
        self.tail.index = tmp2 - 1
   

#проверка работы программы
lst1 = DoubleLink()
lst1.__init__()

print('Сколько значений вы хотите иметь в списке? \n')
k = int(input())
for i in range(k):
    lst1._add_to_tail(10**i)

print("через 5 cекунд будет напечатан список \n")
lst1.display_values()

print("\n какое значение хотите удалить?")
a = int(input())

lst1.delete_node(a-1)
print('\n')
print("через 5 секунд будет напечатан список без удаленного элемента")
print(' ')
lst1.display_values()

print('\n')
print(' поиск значения по индексу \n')
print('введите индекс')
b = int(input())


print('\n значение узла с этим индексом: ')
print(lst1.find_value(b-1))


with open("data_for_lst1.pickle", "wb") as f:   #сериализация
    pickle.dump(lst1, f)

with open("data_for_lst1.pickle", "rb") as f:   # десериализация
    p = pickle.load(f)
print('\n Список после загрузки из файла: \n')
p.display_values()



