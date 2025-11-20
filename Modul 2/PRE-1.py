class Hero:

    jumlah = 0
    __privateJumlah = 0

    def __init__(self, name, health):
        self.name = name
        self.health = health

        self.__private = 'private'
        self.__protected = 'protected'

hero_1 = Hero('Cyborg', 100)

print(hero_1.__dict__)
print(Hero._dict_)
print(Hero.__privateJumlah)