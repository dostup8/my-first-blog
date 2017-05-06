

class DBrow:
    """
    реализация отдельного узла
    """

    # идентификатор узла в дереве ( начиная с нуля )
    id = -1
    ref = -1
    value = ''

    def __init__(self, ref, value):

        self.ref = ref
        self.value = value



class DBemul:
    """
    реализация представления дерева
    """

    # хранит идентификатор для присвоения очередному узлу
    cid = 0

    # массив для хранения узлов
    a = []


    def __init__(self, a):
        """
        инициализация дерева ( и его узлов )
        """

        for i in a:
            i.id = self.cid
            self.a.append(i)
            self.cid += 1


    def addItem(self, item):
        """
        добавить узел
        """

        # присвоили узлу идентификатор
        item.id = self.cid

        self.a.append(item)

        # идентификатор для присвоения последующему узлу
        self.cid += 1


    def delete(self, key):
        """
        удалить узел, зная его id
        :param key:
        :return:
        """

        for i in self.a:

            if i.id == key:
                self.a.remove(i)
                return


    def selectById(self, term):
        """
        выбрать узлы по известному идентификатору id
        :param term:
        :return:
        """

        for i in self.a:
            if i.id == term: return i


    def selectByRef(self, term):
        """
        выбрать узлы, у которых определенное значение ссылки
        :param term:
        :return:
        """
        a = []

        for i in self.a:

            if i.ref == term: a.append(i)
        return a



def getChildren(db, ref):
    """
    получить дочерние узлы
    :param db: дерево с массивом узлов
    :param ref: ссылка на идентификатор узла
    :return:
    """

    # находим первоначальные узлы по идентификатору
    ca = a = db.selectByRef(ref)

    # если такие узлы нашлись
    if(len(a) > 0):

        # для каждого из них по порядку находим дочерние узлы
        for i in a:
            ca.extend(getChildren(db, i.id))
        return ca

    else:
        return ca


def getValuesInChildren(db, id):
    """
    получить значения лисьтев из поддеревьев
    :param db: дерево
    :param id: идентификатор узла
    :return:
    """

    # получить узлы с данным идентификатором
    a = getChildren(db, id)
    res = []

    for i in a:
        res.append(i.value)

    return res




#===========

db = DBemul([
    DBrow(-1, 'root'),
    DBrow(0, '1st node'),
    DBrow(0, '2nd node'),
    DBrow(2, '3rd node'),
    DBrow(1, '4th node'),
    DBrow(2, '5th node')])


print(getValuesInChildren(db, 0))
input('...')



