from classes import Orc, Troll, Dragon, Marcos, Warrior, Mage, Elf

class Battle_levels:
    def __init__(self):
        self.levels = []
        self.add_levels()

    def add_levels(self):
        i = 0
        my_levels = [1, 1.2, 1.3, 1, 1.2, 1.3, 1, 1.2, 1.3, 1]
        while True:
            monster = None
            if i == 10:
                break
            if i < 3:
                monster = Orc.create_default_orc()
            elif i >= 3 and i < 6:
                monster = Troll.create_default_troll()
            elif i >= 6 and i < 9:
                monster = Dragon.create_default_dragon()
            elif i == 9:
                monster = Marcos.create_default_marcos()
            monster.char_upskill(my_levels[i])
            self.levels.append(monster)
            i+=1

class My_save:
    def __init__(self):
        # self.saves = []
        self.saves = [[Warrior.create_default_warrior(), Mage.create_default_mage(), Elf.create_default_elf()]]

    def add_save(self, character):
        self.saves.append(character)
