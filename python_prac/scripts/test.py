# coding: utf8
class Knight:
    def __init__(self, health, mana, armor):
        self.health = health
        self.mana = mana
        self.armor = armor

    def slash(self):
        print("slash")

class Annie:
    def __init__(self, health, mana, ability_power):
        self.health = health
        self.mana = mana
        self.ability_power = ability_power 
    
    def tibbers(self):
        print("티버 : 피해량 {0}".format(self.ability_power*0.65 + 400))
if __name__=="__main__":
    health, mana, ability_power = map(float, raw_input().split())
    x = Annie(health=health, mana=mana, ability_power=ability_power)
    x.tibbers()
