from classes import Warrior, Mage, Elf, Game
from data import Battle_levels, My_save

import random, os


class Menu:
    def __init__(self):
        self.opcao = None
        self.monsters = Battle_levels()
        self.save = My_save()
        self.menu = """         *** IMPOSSIBLE GAME ***

1 - New Game
2 - Load Game
3 - About

0 - Exit Game
"""
    def execute(self):
        while True:
            print(self.menu)
            self.opcao = (input("Select your option:\n"))
            os.system('clear')
            if self.opcao.isdigit():
                if int(self.opcao) == 1: 
                    self.new_game()
                elif int(self.opcao) == 2:
                    self.load_game()
                elif int(self.opcao) == 3:
                    self.about_game()
                elif int(self.opcao) == 0:
                    break
                else:
                    print("Invalid option. Please choose one of the following options:")
            else:
                print("Invalid option. Please choose one of the following options:")

    def about_game(self):
        print("""
                                    ** About IMPOSSIBLE GAME: **

You are the Hero. Fight your way through 10 levels of monsters and face the ultimate boss! 
Choose your class, fight different monsters and decide if you should keep fighting or run to avoid certain death!
But if you fail... Game Over! But feel free to try again! (You will :D!)
""")

    
    def load_game(self):
        
        while True:
            print("* Saved characters: *\n")
            saved_list = 1
            for item in self.save.saves:
                print(f"[{saved_list}] {item.name} - lvl = {item.level}")
                saved_list += 1
            character = input("Choose your saved game number (select 0 to go back): ")
            os.system('clear')
            if character.isdigit():
                if int(character) == 0:
                    break
                elif int(character) > len(self.save.saves):
                    print("Invalid option. Please choose one of the following saved characters: \n")
                    
                else: 
                    self.hero = self.save.saves[int(character)-1]
                    self.save.saves.remove(self.hero)
                    self.battle(self.hero.level)
                    break
            else:
                print("Invalid option. Please choose one of the saved characters: \n")

        

    def new_game(self):
        level = 1
        heroes = []
        hero_class = None

        self.sub_menu = """
        *** Hero list: ***

1 - Warrior
2 - Mage
3 - Elf

0 - Battle
"""
        while hero_class != 0:
            print(self.sub_menu)
            hero_class = input("Choose your hero Class:\n")
        

            if hero_class.isdigit():
                if int(hero_class) ==1:
                    name = input("Choose your hero name:\n")
                    heroes.append(Warrior(name))
                elif int(hero_class) ==2:
                    name = input("Choose your hero name:\n")
                    heroes.append(Mage(name))
                elif int(hero_class) ==3:
                    name = input("Choose your hero name:\n") 
                    heroes.append(Elf(name))
                elif int(hero_class) ==0:
                    game = Game(heroes)
                    game.battle()
                else:
                    print("Invalid option. Please choose one of the following options:")
                    continue                
                os.system('clear')
                # self.battle(level)
                break           
            else:
                print("Invalid option. Please choose one of the following options:")
   
    def battle(self, level):
        turn = 0
        monster = self.monsters.levels[level-1]
        hero_hp = self.hero.hp
        monster_hp = monster.hp
        flag = True
        while hero_hp > 0 and monster_hp > 0:
            turn += 1
            print(f"""
    ** Level {level} **""")
            print(f"""
     * Round {turn} *
     
Current stats: {self.hero.name} HP = {hero_hp} // {monster.name} HP = {monster_hp}
*****
""")
            hero_hp , monster_hp = self.damage_calculation(monster, hero_hp, monster_hp, flag)
            flag = True

            print(f"""
     * End round * 
                  
{self.hero.name} HP = {hero_hp} // {monster.name} HP = {monster_hp}
\n""")
            if hero_hp > 0 and monster_hp > 0 and input("*** If you want to run from the battle, press (0), otherwise press any key ***: ") == "0":
                if self.run_forrest_run():
                    os.system('clear')
                    print("*** Great Success! You are officially a coward -.-' *** \n")
                    self.save.add_save(self.hero)
                    break
                else:
                    os.system('clear')
                    print(f" *** Failed to run from {monster.name}. Now prepare for the consequences... *** \n")
                    flag = False
            elif monster_hp > 0:
                os.system('clear')

        if hero_hp <= 0:
            print("GAME OVER!!")
        elif monster_hp <= 0:
            if level < 10: 
                self.hero.char_upskill(1.2)
                level += 1
                self.hero.level = level
                if input(f"//Level {self.hero.level - 1} done! Press (0) to save and return to the main menu, otherwise press any key. *** ") == "0":
                    self.save.add_save(self.hero)
                    os.system('clear')
                    return
                print("********************************** Well done! Prepare for the next level. **********************************\n")

                self.battle(level)
            else:
                print("""**** Congratulations!! You have beat the Game! ****
**** Now try to beat with all classes (If you can...) ****
                      """)
                
            

    def damage_calculation(self, monster, hero_hp, monster_hp, flag):
        if flag:
            hero_attack = self.hero.random_attack()
            hero_attack_value = self.hero.char_atk_value(hero_attack)
            print("Battle Phase:\n")
            print("*****")
            print(f"{self.hero.name} attacked with {hero_attack} - {hero_attack_value} atk!\n")
            def_monster = monster.char_def_value(self.hero)
            evade = monster.evade()
            if hero_attack_value > def_monster:
                monster_hp -= (hero_attack_value - def_monster) * evade
                print(f"""***{monster.name} evaded the attack!***
                      ---\n""" if evade == 0 else f"""{monster.name} took {hero_attack_value - def_monster} damage! 
                      ---\n""")
            else:
                print("No damage made, you are too weak!")
        else:
            print(f"******If you can't run from the {monster.name}, you don't deserve to battle! muahahahahahah 3;) ******\n ")
        
        monster_attack = monster.random_attack()
        monster_attack_value = monster.char_atk_value(monster_attack)
        print(f"{monster.name} attacked with {monster_attack} - {monster_attack_value} atk!\n")
        def_hero = 0
        if flag:
            def_hero = self.hero.char_def_value(monster)
        evade = self.hero.evade()
        if monster_attack_value > def_hero:
            hero_hp -= (monster_attack_value - def_hero) * evade
            print(f"""***{self.hero.name} evaded the attack!***
                      ---\n""" if evade == 0 else f"""{self.hero.name} took {monster_attack_value - def_hero} damage! 
                      ---\n""")
        else:
            print("No damage made, this monster is too weak!")
        return hero_hp , monster_hp
    
    def run_forrest_run(self):
        probabilities = [0.5, 0.5]
        run_chance = [True, False]
        run = random.choices(run_chance, probabilities)[0]
        return run


## inicio do programa
menu = Menu()
menu.execute()