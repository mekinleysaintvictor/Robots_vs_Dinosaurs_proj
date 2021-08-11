class Dinosaur:
    def __init__(self):
        self.name = ''
        self.health = 100
        self.attack = 17

    #======= GETTER AND SETTER FOR NAME =========
    def get_dinosaur_name(self):
        return self.name

    def set_dinosaur_name(self, name):
        self.name = name

    #======= GETTER AND SETTER FOR HEALTH =========
    def get_dinosaur_health(self):
        return self.health

    def set_dinosaur_health(self, health):
        self.health = health
    
    #======= GETTER AND SETTER FOR ATTACK POWER ========
    def get_dinosaur_attack(self):
        return self.attack

    def set_dinosaur_attack(self, attack):
        self.attack = attack