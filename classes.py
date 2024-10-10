import random

class Character:
    def __init__(self, **character):
        self.name = character["name"]
        self.hp = character["hp"]
        self.ph_dmg = character["ph_dmg"]
        self.mag_dmg = character["mag_dmg"]
        self.ph_armor = character["ph_armor"]
        self.mag_armor = character["mag_armor"]
        self.attacks = []
        self.level = 1

    def char_status(self):
        print(self.name, self.hp)
    
    def char_upskill(self, value = 1):  
        self.hp = int(self.hp * value)
        self.ph_dmg = int(self.ph_dmg * value)
        self.mag_dmg = int(self.mag_dmg * value)
        self.ph_armor = int(self.ph_armor * value)
        self.mag_armor = int(self.mag_armor * value)
    
    def char_def_value(self, character):
        if isinstance(character, Warrior) or isinstance(character, Orc) or isinstance(character, Troll):
            return self.ph_armor
        if isinstance(character, Mage):
            return self.mag_armor
        if isinstance(character, Dragon) or isinstance(character, Elf) or isinstance(character, Marcos):
            return self.ph_armor + self.mag_armor
        
    def random_attack(self):
        probabilities = [0.85, 0.15]
        attack = random.choices(self.attacks, probabilities)[0]
        return attack
    
    def evade(self):
        probabilities = [0.9, 0.1]
        evade_chance = [1, 0]
        evade = random.choices(evade_chance, probabilities)[0]
        return evade


class Warrior(Character):
    def __init__(self, **warrior):
        super().__init__(**warrior)
        self.attacks = ["Sword Attack", "*Special Attack* - Sword Mastery of Kings"]

    def create_default_warrior(char_name="Warrior"):
        return Warrior(name=char_name, hp=100, ph_dmg=12, mag_dmg=2, ph_armor=10, mag_armor=3)
    
    def char_atk_value(self, attack):
        if self.attacks[0] == attack:
            return self.ph_dmg
        else:
            return self.ph_dmg*2
    
class Mage(Character):
    def __init__(self, **mage):
        super().__init__(**mage)
        self.attacks = ["Magic Attack", "*Special Attack* - Enchantment of the Havens"]

    def create_default_mage(char_name="Mage"):
        return Mage(name=char_name, hp=60, ph_dmg=2, mag_dmg=15, ph_armor=3, mag_armor=10)  

    def char_atk_value(self, attack):
        if self.attacks[0] == attack:
            return self.mag_dmg
        else:
            return self.mag_dmg*2

class Elf(Character):
    def __init__(self, **elf):
        super().__init__(**elf)
        self.attacks = ["Lightning Arrow", "*Special Attack* - Killing Zone"]

    def create_default_elf(char_name="Elf"):
        return Elf(name=char_name, hp=100, ph_dmg=8, mag_dmg=7, ph_armor=6, mag_armor=6)  
    
    def char_atk_value(self, attack):
        if self.attacks[0] == attack:
            return self.ph_dmg + self.mag_dmg
        else:
            return (self.ph_dmg + self.mag_dmg)*2

class Orc(Character):
    def __init__(self, **orc):
        super().__init__(**orc)
        self.attacks = ["Charge Attack", "*Special Attack* - Battle Cry"]

    def create_default_orc():
        return Orc(name="Orc", hp=50, ph_dmg=15, mag_dmg=1, ph_armor=2, mag_armor=2)  

    def char_atk_value(self, attack):
        if self.attacks[0] == attack:
            return self.ph_dmg
        else:
            return self.ph_dmg*2

class Troll(Character):
    def __init__(self, **troll):
        super().__init__(**troll)
        self.attacks = ["Slash Attack", "*Special Attack* - Berserker Rage"]

    def create_default_troll():
        return Troll(name="Troll", hp=250, ph_dmg=20, mag_dmg=1, ph_armor=10, mag_armor=1)  
    
    def char_atk_value(self, attack):
        if self.attacks[0] == attack:
            return self.ph_dmg
        else:
            return self.ph_dmg*2

class Dragon(Character):
    def __init__(self, **dragon):
        super().__init__(**dragon)
        self.attacks = ["Fire Breath" , "*Special Attack* - Dragon Pulse"]

    def create_default_dragon():
        return Dragon(name="Dragon", hp=500, ph_dmg=30, mag_dmg=10, ph_armor=10, mag_armor=10)
    
    def char_atk_value(self, attack):
        if self.attacks[0] == attack:
            return self.ph_dmg + self.mag_dmg
        else:
            return (self.ph_dmg + self.mag_dmg)*2

class Marcos(Character):
    def __init__(self, **marcos):
        super().__init__(**marcos)
        self.attacks = ["Beleza?", "*Special Attack* - Alguém tem dúvidas?"]

    def create_default_marcos():
        return Marcos(name="Marcos", hp=1000, ph_dmg=10, mag_dmg=10, ph_armor=20, mag_armor=20)

    def char_atk_value(self, attack):
        if self.attacks[0] == attack:
            return self.ph_dmg + self.mag_dmg
        else:
            return (self.ph_dmg + self.mag_dmg)*5

