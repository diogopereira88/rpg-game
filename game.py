from classes import Warrior, Mage, Elf
from data import Battle_levels, My_save

import random, os


class Menu:
    def __init__(self):
        self.opcao = None
        self.heroes = []
        self.monsters = Battle_levels()
        self.save = My_save()
        self.menu = """         🎮 My RPG Game 🎮


1️⃣ - New Game 
2️⃣ - Load Game
3️⃣ - About

0️⃣ - Exit Game 🛑
"""
    def execute(self):
        while True:
            print(self.menu)
            self.opcao = (input("・Select your option: \n"))
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
                    print("❌ Invalid option. Please choose one of the following options:")
            else:
                print("❌ Invalid option. Please choose one of the following options:")

    def about_game(self):
        print("""
                                  📝 About My RPG Game:

You are the Hero. 
Fight your way through 10 levels of monsters and face the ultimate boss! 
Choose your class, how many heroes you want in your party and fight different monsters!
Keep fighting between turns or run/regroup to avoid certain death!
But if you fail... Game Over! But feel free to try again! (You will 😁!)
""")

    
    def load_game(self):
        
        while True:
            print("Saved games: \n")
            saved_list = 1
            for item in self.save.saves:
                print(f"🎮 [{saved_list}] - ", end="")
                for hero in item:
                    print(f"{hero.name} ・ ", end="")
                print(f"( lvl {item[0].level})")
                saved_list += 1
            character = input("Choose your saved game number (select 0 to go back): ")
            os.system('clear')
            if character.isdigit():
                if int(character) == 0:
                    break
                elif int(character) > len(self.save.saves):
                    print("❌ Invalid option. Please choose one of the following saved characters: \n")
                    
                else: 
                    self.heroes = self.save.saves[int(character)-1]
                    self.save.saves.remove(self.heroes)
                    self.battle(self.heroes[0].level)
                    break
            else:
                print("❌ Invalid option. Please choose one of the saved characters: \n")

        

    def new_game(self):
        self.heroes = []
        level = 1
        self.sub_menu = """
      •••   Hero Class list:   •••

1 - Warrior 🗡️
2 - Mage 🪄
3 - Elf 🏹

"""
        while True:
            print(self.sub_menu)
            hero_class = input("・Choose your Hero Class 1️⃣ , 2️⃣ , 3️⃣ :\n")
        

            if hero_class.isdigit():
                if int(hero_class) ==1:
                    name = input("・Choose your hero name:\n")
                    self.heroes.append(Warrior.create_default_warrior(name))
                    self.other_chars()
                elif int(hero_class) ==2:
                    name = input("・Choose your hero name:\n")
                    self.heroes.append(Mage.create_default_mage(name))
                    self.other_chars()
                elif int(hero_class) ==3:
                    name = input("・Choose your hero name:\n") 
                    self.heroes.append(Elf.create_default_elf(name))
                    self.other_chars()
                elif int(hero_class) ==0:
                    os.system('clear')
                    break
                else:
                    print("❌ Invalid option. Please choose one of the following options:")
                    continue
                
                os.system('clear')
                self.battle(level)
                break           
            else:
                os.system('clear')
                # print("❌ Invalid option. Please choose one of the following options:")
        
                

    def other_chars(self):
        while True:
            print()
            hero_class = input("・Choose your other hero Class (select 0️⃣  if you don't want any other heroes in your party):\n")
            if hero_class.isdigit():
                if int(hero_class) ==1:
                    name = input("・Choose your hero name:\n")
                    self.heroes.append(Warrior.create_default_warrior(name))
                elif int(hero_class) ==2:
                    name = input("・Choose your hero name:\n")
                    self.heroes.append(Mage.create_default_mage(name))
                elif int(hero_class) ==3:
                    name = input("・Choose your hero name:\n") 
                    self.heroes.append(Elf.create_default_elf(name))
                elif int(hero_class) ==0:
                    break
                else:
                    os.system('clear')
                    print(self.sub_menu)
                    print("❌ Invalid option.")
                    continue
            else:
                os.system('clear')
                print(self.sub_menu)
                print("❌ Invalid option.")
               


    
    def battle(self, level):
        turn = 0
        monster = self.monsters.levels[level-1]
        heroes_hp = [hero.hp for hero in self.heroes]
        monster_hp = monster.hp
        flag = True
        while len(self.heroes) > 0 and monster_hp > 0:
            turn += 1
            i = 0
            heroes_current_status = ""
            for hero in self.heroes:
                heroes_current_status += " ・ " + hero.name + " HP = " + str(heroes_hp[i])
                i+=1
            print(f"""  
    ✹ Level {level} ✹""")
            print(f"""
                  
   ・ Round {turn} ・

     
Current stats: {heroes_current_status}  / ・{monster.name} HP = {monster_hp}
""")
            
            print(" 🗡️  Battle Phase 🗡️\n")
            heroes_hp , monster_hp = self.damage_calculation(monster, heroes_hp, monster_hp, flag)
            flag = True
            heroes_current_status = ""
            i = 0
            for hero in self.heroes:
                heroes_current_status += " ・ " + hero.name + " HP = " + str(heroes_hp[i])
                i+=1
            print(f"""
     ✹ End round ✹ 
                
Current stats: {heroes_current_status}  / ・{monster.name} HP = {monster_hp}
\n""")
            if len(heroes_hp) > 0 and monster_hp > 0 and input("*** If you want to run from the battle press 0️⃣ , otherwise press any key ***: ") == "0":
                if self.run_forrest_run():
                    os.system('clear')
                    print("*** Great Success! You are officially a coward... 😒 *** \n")
                    self.save.add_save(self.heroes)
                    break
                else:
                    os.system('clear')
                    print(f" *** Failed to run from {monster.name}. Now prepare for the consequences... 😈 *** \n")
                    flag = False
            elif monster_hp > 0:
                os.system('clear')

        if len(heroes_hp) <= 0:
            print("GAME OVER!! 💀💀")
        elif monster_hp <= 0:
            if level < 10:
                level += 1
                for hero in self.heroes:
                    hero.char_upskill(1.2)
                    hero.level = level
                if input(f"*** Level {level - 1} cleared! ✅ All your heroes stats improved 20%! 💪 Press 0️⃣  to save and return to the main menu, otherwise press any key. *** ") == "0":
                    self.save.add_save(self.heroes)
                    os.system('clear')
                    return
                print("********************************** Well done! 🙌  Prepare for the next level. **********************************\n")
                os.system('clear')
                self.battle(level)
            else:
                os.system('clear')
                print("""**** 🏆 Congratulations!! 🏆 You have beat the Game! ****
**** Now try to beat solo with all classes (If you can...😏) ****
                      """)
                
            

    def damage_calculation(self, monster, heroes_hp, monster_hp, flag):
        index = 0
        for hero in self.heroes:
            if flag:
                hero_attack = hero.random_attack()
                hero_attack_value = hero.char_atk_value(hero_attack)
                
                print("________________________________")
                print(f"{hero.name} attacked with {hero_attack} - {hero_attack_value} atk!\n")
                def_monster = monster.char_def_value(hero)
                evade = monster.evade()
                if hero_attack_value > def_monster:
                    monster_hp -= (hero_attack_value - def_monster) * evade
                    print(f"""・・{monster.name} evaded the attack!・・
                        ---\n""" if evade == 0 else f"""{monster.name} took {hero_attack_value - def_monster} damage! 
                        ---\n""")
                else:
                    print("No damage made, you are too weak!")
            else:
                print(f"**If you can't run from the {monster.name}, you don't deserve to battle! 😈 ******\n ")
        
            monster_attack = monster.random_attack()
            monster_attack_value = monster.char_atk_value(monster_attack)
            print(f"{monster.name} attacked with {monster_attack} - {monster_attack_value} atk!\n")
            def_hero = 0
            if flag:
                def_hero = hero.char_def_value(monster)
            evade = hero.evade()
            if monster_attack_value > def_hero:
                heroes_hp[index] -= (monster_attack_value - def_hero) * evade
                print(f""" ・・{hero.name} evaded the attack!・・
                        ---\n""" if evade == 0 else f"""{hero.name} took {monster_attack_value - def_hero} damage! 
                        ---\n""")
                if heroes_hp[index] <=0:
                    print(f"💀 {hero.name} died! 💀")
            else:
                print("No damage made, this monster is too weak!")
            index+=1
        index = 0
        while(index < len(heroes_hp)):
            if heroes_hp[index] < 0:
                heroes_hp.pop(index)
                self.heroes.pop(index)
            else:
                index+=1
        return heroes_hp, monster_hp
    
    def run_forrest_run(self):
        probabilities = [0.5, 0.5]
        run_chance = [True, False]
        run = random.choices(run_chance, probabilities)[0]
        return run


## inicio do programa
menu = Menu()
menu.execute()