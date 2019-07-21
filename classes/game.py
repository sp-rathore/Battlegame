import random
from classes.magic import Spell
from classes.inventory import Item
import pprint

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


class Person:
    def __init__(self, name, hp, mp, atk, df, magic, items):
        self.name = name
        self.maxhp = hp
        self.hp = hp
        self.maxmp = mp
        self.mp = mp
        self.atkl = atk - 10
        self.atkh = atk + 10
        self.df = df
        self.magic = magic
        self.actions = ["Attack", "Magic", "Items"]
        self.items = items

    def generate_damage(self):
        return random.randrange(self.atkl, self.atkh)

    def take_damage(self, dmg):
        self.hp -= dmg
        if self.hp < 0:
            self.hp = 0
        return self.hp

    def heal(self, dmg):
        self.hp += dmg
        if self.hp > self.maxhp:
            self.hp = self.maxhp

    def get_hp(self):
        return self.hp

    def get_max_hp(self):
        return self.maxhp

    def get_mp(self):
        return self.mp

    def get_max_mp(self):
        return  self.maxmp

    def reduce_mp(self, cost):
        self.mp -= cost


    def choose_action(self):
        i = 1
        print("\n" + "    " + bcolors.BOLD + self.name + bcolors.ENDC)
        print(bcolors.OKBLUE + bcolors.BOLD + "     ACTIONS:" + bcolors.ENDC)
        for item in self.actions:
            print("      " + str(i) + ":", item)
            i +=1

    def choose_magic(self):
        i = 1
        print("\n" + bcolors.OKBLUE + bcolors.BOLD + "     MAGIC:" + bcolors.ENDC)
        #print("\n" , self.magic[0][0])
        for spell in self.magic:
            print("      " +str(i) + ":", spell.name, "(cost:", str(spell.cost) +   ")")
            i += 1

    def choose_items(self):
        i = 1
        print("\n" + bcolors.OKBLUE + bcolors.BOLD + "     Items:" + bcolors.ENDC)
        for item in self.items:
            print("      " + str(i) + ":", item["item"].name + ":", item["item"].description, " (x " + str(item["quantity"]) + ")")
            i += 1

    def chose_target(self, enemies):
        i = 1
        print("\n" + bcolors.FAIL + bcolors.BOLD + "     Targets:" + bcolors.ENDC)

        for enemy in enemies:
            print("      " + str(i) + ":", enemy.name )
            i += 1
        enemy_choice = int(input("    Please provide Enemy Target:")) - 1
        return enemy_choice

    def get_enemy_stats(self):
        hp_enemy_bar = ""
        hp_enemy_bar_ticks = (self.hp / self.maxhp) * 100 / 2

        while hp_enemy_bar_ticks > 0:
            hp_enemy_bar += "█"
            hp_enemy_bar_ticks -= 1

        while len(hp_enemy_bar) < 50:
            hp_enemy_bar += " "

        hp_enemy_string = str(self.hp) + "/" + str(self.maxhp)
        current_hp_enemy_string = ""

        if len(hp_enemy_string) < 11:
            delta_enemy_string = 11 - len(hp_enemy_string)

            while delta_enemy_string > 0:
                current_hp_enemy_string += " "
                delta_enemy_string -= 1

            current_hp_enemy_string += hp_enemy_string
        else:
            current_hp_enemy_string = hp_enemy_string

        print("                         __________________________________________________")
        print(bcolors.BOLD + self.name + "    " + current_hp_enemy_string + "  |" + bcolors.FAIL + hp_enemy_bar + bcolors.ENDC + "|")

    def get_stats(self):
        hp_bar = ""
        hp_bar_ticks = (self.hp/self.maxhp) * 100 / 4

        mp_bar = ""
        mp_bar_ticks = (self.mp/self.maxmp) * 100 / 10

        while hp_bar_ticks > 0:
            hp_bar += "█"
            hp_bar_ticks -= 1

        while len(hp_bar) < 25:
            hp_bar += " "

        while mp_bar_ticks > 0:
            mp_bar += "█"
            mp_bar_ticks -= 1

        while len(mp_bar) < 10:
            mp_bar += " "

        hp_string = str(self.hp) + "/" + str(self.maxhp)
        current_hp_string = ""

        if len(hp_string) < 9:
            delta_string = 9 - len(hp_string)

            while delta_string > 0:
                current_hp_string += " "
                delta_string -= 1

            current_hp_string += hp_string
        else:
            current_hp_string = hp_string

        mp_string = str(self.mp) + "/" + str(self.maxmp)
        current_mp_string = ""

        if len(mp_string) < 7:
            delta_mp_string = 7 - len(mp_string)

            while delta_mp_string > 0:
                current_mp_string += " "
                delta_mp_string -= 1

            current_mp_string += mp_string
        else:
            current_mp_string = mp_string

        print("                         _________________________          __________")
        print(bcolors.BOLD + self.name + "        " + current_hp_string + "  |" + bcolors.OKGREEN +  hp_bar + bcolors.ENDC + "| " +
              bcolors.BOLD + current_mp_string + "|" + bcolors.OKBLUE + mp_bar + "|" + bcolors.ENDC)


