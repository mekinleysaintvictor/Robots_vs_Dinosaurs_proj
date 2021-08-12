from weapon import Weapon

class Robot:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.weapon = Weapon("sword", 10)

    # ======== GETTER AND SETTER FOR NAME ===========
    def get_robot_name(self):
        return self.name

    def set_robot_name(self, name):
        self.name = name
    
    # ======== GETTER AND SETTER FOR HEALTH ==========
    def get_robot_health(self):
        return self.health
    
    def set_robot_health(self, health):
        self.health = health

   # ======== GETTER AND SETTER FOR WEAPON ===========

    def get_robot_weapon(self):
       return self.weapon.get_weapon_name()

    def set_robot_weapon(self):
        self.weapon.set_weapon_name()