from classes.game import Person, bcolors
from classes.magic import Spell
from classes.inventory import Item
import random

'''
magic = [{"name": "Fire", "cost" :"10", "dmg" : 60},
         {"name": "Thunder", "cost" :"10", "dmg" : 80},
         {"name": "Blizzard", "cost" :"10", "dmg" : 70}]
'''

print("\n \n")


# Creat Black Magic

fire = Spell("Fire", 10, 800, "black")
thunder = Spell("Thunder", 10, 520, "black")
blizzard = Spell("Blizzard", 10, 700, "black")
meteor = Spell("Meteor", 20, 1600, "black")
quake = Spell("Quake", 14, 540, "black")


# Creat White Magic

cure = Spell("Cure", 12, 620, "white")
cura = Spell("Cura", 18, 1500, "white")

'''
magic = [{"name": "Fire", "cost" :"10", "dmg" : 100},
         {"name": "Thunder", "cost" :"10", "dmg" : 120},
         {"name": "Blizzard", "cost" :"10", "dmg" : 100}]
'''

## Create some Items

potion = Item("Potion", "potion", "heals 50 HP", 50)
hipotion = Item("Hi-Potion", "potion", "heals 100 HP", 100)
superpotion = Item("Super-Potion", "potion", "heals 1000 HP", 1000)
elixir = Item("Elixir", "elixir", "Fully restores HP/MP of one party member heals 50 HP", 9999)
megaelixir = Item("MegaElixir", "elixir", "Fully restores HP/MP of party's", 9999)

grenade = Item("Grenade", "attack", "Deals 500 damage", 500)


# Instantiate People

player_spells = [fire, thunder, blizzard, meteor, cure, cura]
#player_items =  [potion, hipotion, superpotion, elixir, megaelixir, grenade]
player_items =  [{"item": potion, "quantity": 15},{"item": hipotion, "quantity": 5}, {"item": superpotion, "quantity": 5},
                 {"item": elixir, "quantity": 5}, {"item": megaelixir, "quantity": 2}, {"item": grenade, "quantity": 5}]
player1 = Person("Valos", 3460, 135, 60, 34, player_spells, player_items)
player2 = Person("Nick ", 4160, 189, 60, 34, player_spells, player_items)
player3 = Person("Robot", 3280, 175, 60, 34, player_spells, player_items)

players = [player1, player2, player3]

'''
print(player.generate_damage())
print(player.generate_damage())
print(player.generate_damage())
print(player.generate_spell_damage(0))
print(player.generate_spell_damage(1))
'''
# Instantiate Enemy

enemy1 = Person("Imp1 :", 1200, 850,45, 25, [], [])
enemy2 = Person("Magus :", 20000, 850,45, 25, [], [])
enemy3 = Person("Imp2 :", 1200, 850,45, 25, [], [])

enemies = [enemy1, enemy2, enemy3]

running = True
i = 0

#print(bcolors.FAIL + bcolors.BOLD + "An Enemy Attack" + bcolors.ENDC)

while running:
    #print("Lets overflow the stack", i)
    #i+ = 1
#    print("===============================")

    #player.choose_magic()


    print("\n\n")
    print(bcolors.BOLD + " Name                           HP                            MP" + bcolors.ENDC)
    for player in players:
        print(player.get_stats())
    print("\n")
    #print("Your choice entered is: ", player.get_spell_name(int(choice)))

    for enemy in enemies:
        enemy.get_enemy_stats()

    for player in players:
        player.choose_action()
        choice = input("      Please Enter Choice: ")
        index = int(choice) - 1

        if index == 0:
            dmg = player.generate_damage()
            target_enemy = player.chose_target(enemies)
            print("    The damage is :", str(dmg))
            enemies[target_enemy].take_damage(dmg)
            print("    You attacked " +  enemies[target_enemy].name + "for, ", dmg, "points of damage. Enemy HP is:", enemy.get_hp())
        #running = False

        elif index == 1:
            player.choose_magic()
            magic_choice = int(input(" Choose Magic :")) - 1
            #magic_dmg = player.magic[magic_choice].generate_damage

            if magic_choice == -1:
                continue

            spell = player.magic[magic_choice]
            magic_dmg = spell.generate_damage()


            current_mp = player.get_mp()

            if spell.cost > current_mp:
                print(bcolors.FAIL + "\n Not Enough MP \n" + bcolors.ENDC)
                continue

            player.reduce_mp(spell.cost)

            if spell.type == "white":
                player.heal(magic_dmg)
                print(bcolors.OKBLUE + "\n" + spell.name + "heals for", str(magic_dmg), " HP" + bcolors.ENDC)

            elif spell.type == "black":

                target_enemy = player.chose_target(enemies)
                #print("    The damage is :", str(dmg))

                enemies[target_enemy].take_damage(magic_dmg)

                print(bcolors.OKBLUE + "\n" + spell.name + "deals for", str(magic_dmg), " points of damage." + bcolors.ENDC)

            #enemy.take_damage(magic_dmg)
            #print(bcolors.OKBLUE + "\n" + spell.name + "deals ", str(magic_dmg), "points of damage" + bcolors.ENDC)

        elif index == 2:
            player.choose_items()
            item_choice = int(input("Choose Item: ", )) - 1

            if item_choice == -1:
                continue

            item = player.items[item_choice]["item"]

            if player.items[item_choice]["quantity"] == 0:
                print(bcolors.FAIL + "\n" + "None Left for further play ", bcolors.ENDC)
                continue

            player.items[item_choice]["quantity"] -= 1

            if item.type == "potion":
                player.heal(item.prop)
                print(bcolors.OKGREEN + "\n" + item.name + "heals for ", str(item.prop), "HP", bcolors.ENDC)

            elif item.type == "elixir":
                if item.name == "megaelixir":
                    for i in players:
                        i.hp = i.maxhp
                        i.mp = i.maxmp
                else:
                    player.hp = player.maxhp
                    player.mp = player.maxmp
                print(bcolors.OKGREEN  + "\n" + item.name + "Full restores HP/MP ", bcolors.ENDC)

            elif item.type == "attack":
                target_enemy = player.chose_target(enemies)

                enemies[target_enemy].take_damage(item.prop)
                print(bcolors.FAIL + "\n" + item.name + "deals ", str(item.prop), "points of damage to" + enemies[target_enemy].name + bcolors.ENDC)

    enemy_choice = 1

    target = random.randrange(0,3)

    enemy_dmg = enemies[0].generate_damage()
    players[target].take_damage(enemy_dmg)
    #print("Enemy attacked Player for: ", enemy_dmg, "point of damage. Player HP :", player.get_hp())

    print("Enemy attacked Player for: ", enemy_dmg)

    print(" -----------------------------   ")
    print("Enemy HP: ", bcolors.FAIL + str(enemy.get_hp()) + "/" + str(enemy.get_max_hp()) + bcolors.ENDC + "\n")
   # print("Your HP: ", bcolors.OKGREEN + str(player.get_hp()) + "/" + str(player.get_max_hp()) + bcolors.ENDC + "\n")
   # print("Your MP: ", bcolors.OKBLUE + str(player.get_mp()) + "/" + str(player.get_max_mp()) + bcolors.ENDC + "\n")

    if enemy.get_hp() == 0:
        print( bcolors.OKGREEN + "You have won! " + bcolors.ENDC)
        running = False
    elif player.get_hp() == 0:
        print(bcolors.FAIL + "You have Lost! Enemy has won " + bcolors.ENDC)
        running = False

