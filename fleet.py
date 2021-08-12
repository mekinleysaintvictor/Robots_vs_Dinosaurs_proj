from robot import Robot


class Fleet:
    def __init__(self):
        self.name = "Robot Fleet"
        self.robots = []

    def add_robots(self):
        first_robot = Robot("Steve")
        second_robot = Robot("Miranda")
        third_robot = Robot("Julio")
        # first_robot.set_robot_name("Steve")
        # first_robot.set_robot_weapon()
        # second_robot.set_robot_name("Miranda")
        # second_robot.set_robot_weapon()
        # third_robot.set_robot_name("Julio")
        # third_robot.set_robot_weapon()
        self.robots.append(first_robot)
        self.robots.append(second_robot)
        self.robots.append(third_robot)