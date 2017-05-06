class Arr:
    """
    реализация ассоциативного массива
    """

    # хранение элементов Item
    a = []

    # изменен массив или нет
    c = False


    def __init__(self, ea):
        self.a.extend(ea)
        self.c = True


    def add(self, key, value):

        self.a.append(Item(key, value))
        self.c = True


    def delete(self, key):

        for i in self.a:

            if i.key == key:
                self.a.remove(i)
                return str(key) + ' item deleted'

        return 'not exists'


    def getAll(self):
        ba = []
        self.mergeSort()

        for i in self.a:
            ba.append(i.value)

        return ba


    def getItem(self, key):
        self.mergeSort()

        for i in self.a:

            if i.key == key:
                return i.value

        return 'not exists'


    def merge(self, pa):
        k = 0
        na = []

        # проходясь по массиву элементов
        while k < len(pa):
            ca = []
            i = 0
            j = 0

            while True:

                # если элемент k есть в массиве и i не больше количества подэлементов в элементе
                # и
                # если k+1 элемент элемент есть в массиве и j не превышает количество подэлементов
                if len(pa) > k and len(pa[k]) > i and len(pa) > k + 1 and len(pa[k + 1]) > j:

                    # если ключ предыдущего элемента меньше последующего
                    if pa[k][i].key < pa[k + 1][j].key:
                        ca.append(pa[k][i])
                        i += 1

                    else:
                        ca.append(pa[k + 1][j])
                        j += 1

                # если элемент k есть в массиве и i не больше количества подэлементов в элементе
                # или
                # если k+1 элемент элемент есть в массиве и j не превышает количество подэлементов
                elif len(pa) > k and len(pa[k]) > i or len(pa) > k + 1 and len(pa[k + 1]) > j:

                    # если элемент k есть в массиве и i не превышает количества подэлементов в нем
                    if len(pa) > k and len(pa[k]) > i:
                        ca.append(pa[k][i])
                        i += 1

                    else:
                        ca.append(pa[k + 1][j])
                        j += 1

                else:
                    break

            # запоминаем в конечный массив
            na.append(ca)

            # смещаемся на два элемента вперед
            k += 2

        # если в массиве всего один элемент
        if len(na) == 1:
            return na

        else:
            # рекурсивно продолжаем сортировать массив
            return self.merge(na)


    def mergeSort(self):
        """
        сортировка массива
        :return:
        """

        # если с последнего раза массив был изменен
        if self.c:
            na = []

            # для последующей сортировки каждый элемент представляем массивом
            for i in self.a:
                ca = [i]
                na.append(ca)

            # отсортированный массив в первом элементе
            self.a = self.merge(na)[0]

            # массив теперь пока не изменен
            self.c = False



class Item:
    """
    отдельный элемент ассоциативного массива
    """

    key = -1
    value = ''

    def __init__(self, key, val):
        self.key = key
        self.value = val




#====================

# создание массива
arr = Arr([Item(6, 'six'),
           Item(8, 'eight'),
           Item(3, 'three'),
           Item(5, 'five'),
           Item(1, 'one'),
           Item(4, 'four'),
           Item(2, 'two'),
           Item(7, 'seven'),
           Item(9, 'nine')])

# тестирование работы
print(arr.getAll())
arr.add(10, 'ten')
print(arr.getAll())
arr.add(0, 'zero')
print(arr.getAll())

print(arr.getItem(4))
print(arr.delete(4))
print(arr.getAll())

input('...')
