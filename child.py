from parent import Parent


class Child(Parent):
    def name(self):
        return "child"


if __name__ == '__main__':
    Child().hello()
