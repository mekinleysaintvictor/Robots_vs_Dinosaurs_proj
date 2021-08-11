from weapon import Weapon
from robot import Robot


    #======= TESTING WEAPON CLASS ========
robot_sword = Weapon()
robot_raygun = Weapon()
robot_chainsaw = Weapon()

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

    #====== TESTING ROBOT CLASS ======

robot_one = Robot()
robot_one.set_robot_name("Robert")
robot_one.set_robot_weapon()
print(robot_one.get_robot_name())
print(robot_one.get_robot_health())
print(robot_one.get_robot_weapon())