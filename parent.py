from abc import (abstractmethod)


class Parent(object):
    @abstractmethod
    def name(self):
        return "parent"

    def hello(self):
        print("Hello, " + self.name())


if __name__ == '__main__':
    Parent().hello()
