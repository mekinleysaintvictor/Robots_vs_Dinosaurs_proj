from weapon import Weapon


    #======= TESTING WEAPON CLASS ========
robot_sword = Weapon()
robot_raygun = Weapon()
robot_chainsaw = Weapon()
robot_weapon = Weapon()

# NAMING AND SETTING ATACK POWER FOR FIRST WEAPON (SWORD)
robot_sword.set_weapon_name()
print(robot_sword.get_weapon_name())
print(robot_sword.get_weapon_attack())

# NAMING AND SETTING ATTACK POWER FOR SECOND WEAPON (RAYGUN)
robot_raygun.set_weapon_name()
print(robot_raygun.get_weapon_name())
print(robot_raygun.get_weapon_attack())

# NAMING AND SETTING ATTACK POWER FOR THIRD WEAPON (CHAINSAW)
robot_chainsaw.set_weapon_name()
print(robot_chainsaw.get_weapon_name())
print(robot_chainsaw.get_weapon_attack())

# TESTING SET WEAPON DETAILS FUNCTION
# robot_weapon.set_weapon_details()
print(robot_weapon.get_weapon_name())
print(robot_weapon.get_weapon_attack())