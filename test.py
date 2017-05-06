

"""
# doc2
"""
# pylint: disable=too-few-public-methods

class Student:
    """This method does the same as :func:`~mymodule.MyClass.foo`"""

    def __init__(self, name, age, major):
        self.name = name
        self.age = age
        self.major = major

    def is_old(self):
        """This method does the 2 same as :func:`~mymodule.MyClass.foo`"""

        return self.age > 100


print(u'Пример вывода кириллического текста')
