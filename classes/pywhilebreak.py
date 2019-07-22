import random

player_health = 300
attack_lmt_low  = 50
attack_lmt_high = 90

class Enemy():

    hp = 500
    def __init__(self, attack_lmt_low, attack_lmt_high):
        self.attack_lmt_low = attack_lmt_low
        self.attack_lmt_high = attack_lmt_high

    def getAttack(self):
        print("Lower limit of attack is: ", self.attack_lmt_low)
        print("Higher limit of attacj is: ", self.attack_lmt_high)
        print("Health power is: ", self.hp)


enemy1 = Enemy(50,55)
enemy1.getAttack()

enemy2 = Enemy(75,95)
enemy2.getAttack()

'''
while player_health > 0:
    damage_points = random.randrange(attack_lmt_low, attack_lmt_high)
    player_health = player_health - damage_points

    if player_health < 30:
        player_health = 30

    print("Enemy strike has damaged your health by ", damage_points, "and your health points now is: ", player_health)

    if player_health == 30:
        print("Your health has been severely damaged and you are being teleported. Take care! ")
        break
'''
