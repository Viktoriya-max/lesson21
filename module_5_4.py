class House:
    houses_history = []
    def __new__(cls, *args):
        cls.houses_history.append(args[0])
        return super().__new__(cls)

    def __init__(self, name, number_of_floor):
        self.name = name
        self.number_of_floor = number_of_floor

    def go_to(self, new_floor):
        for floor in range(1, new_floor + 1):
            if new_floor > self.number_of_floor or new_floor < 1:
                print('Такого этажа не существует')
                break
            else:
                print(floor)

    def __len__(self):
        return self.number_of_floor

    def __str__(self):
        return f'Название: {self.name}, кол-во этажей: {self.number_of_floor}'

    def __eq__(self, other):
        return self.number_of_floor == other.number_of_floor

    def __lt__(self, other):
        return self.number_of_floor < other.number_of_floor

    def __le__(self, other):
        return self.number_of_floor <= other.number_of_floor

    def __gt__(self, other):
        return self.number_of_floor > other.number_of_floor

    def __ge__(self, other):
        return self.number_of_floor >= other.number_of_floor

    def __ne__(self, other):
        return self.number_of_floor != other.number_of_floor

    def __add__(self, value):
        self.number_of_floor = self.number_of_floor + value
        return self
    def __radd__(self, value):
        self.number_of_floor = value + self.number_of_floor
        return self

    def __iadd__(self, value):
        self.number_of_floor += value
        return self

    def __del__(self):
        print(f'{self.name} снесен, но он останется в истории')

h1 = House('"Дом"', 5)
print(House.houses_history)

h2 = House('"Небоскреб"', 38)
print(House.houses_history)

h3 = House('"Шалаш"', 1)
print(House.houses_history)

#Удаление объектов
del h2
del h3

print(House.houses_history)
