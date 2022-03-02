class Item:
    def __init__(self, x, y) -> None:
        assert x is int and y is int, f"Argument 'x' and 'y' should be an integer."
        self.x = x
        self.y = y

    def add(self):
        return self.x + self.y

a = Item(x=1, y='5')
sum = a.add()
print(sum)