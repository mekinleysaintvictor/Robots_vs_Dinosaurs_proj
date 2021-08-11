class Weapon:
    # ======== CONSTRUCTOR ==========

    def __init__(self):
        self.name = ''
        self.attack = 0

    # def set_weapon_details(self, name):
    #     self.name = name
    #     self.attack = self.set_attack_power()

    # ======= GETTER AND SETTER FOR WEAPON NAME ========

    def get_weapon_name(self):
        return self.name
        
    def set_weapon_name(self):
        name = input("Choose your weapon: sword, ray gun, or chainsaw ")
        if(name.lower() == "sword"):
            self.name = name
            self.set_attack_power()
        elif(name.lower() == "ray gun"):
            self.name = name
            self.set_attack_power()
        elif(name.lower() == "chainsaw"):
            self.name = name
            self.set_attack_power()
        else:
            self.name = ""

    # ======= GETTER AND SETTER FOR WEAPON ATTACK POWER ========

    def get_weapon_attack(self):
        return self.attack

    def set_attack_power(self):
        if(self.name == "chainsaw"):
            self.attack = 15
        elif(self.name == "ray gun"):
            self.attack = 12
        else:
            self.attack = 10
