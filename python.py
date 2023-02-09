import random
class Student:
    def __init__(self,name):
        self.name = name
        self.gladness = 50
        self.progress = 0
        self.alive = True


    def to_study(self):
        print("Time to study")
        self.progress += 0.12
        self.gladness -= 3
    def to_work(self):
        print("I need go work")
        self.progress -= 5
        self.gladness += 2

    def to_sleep(self):
        print("I will sleep")
        self.gladness += 3


    def to_chill(self):
        print("Rest time")
        self.gladness += 5
        self.progress -= 0.1


    def to_alive(self):
        if self.progress < -0.5:
            print("Cash out..")
            self.alive = False
        elif self.gladness <= 0:
            print("Depresion")
            self.alive = False
        elif self.progress > 5:
            print("Passed externally")
            self.alive = False

    def end_of_day(self):
        print(f"Gladness = {self.gladness}")
        print(f"Progress = {round(self.progress, 2)}")
    def life(self, day):
        day = "Day" + str(day) + "of" + self.name + "life"
        print(f"{day:=^50}")
        life_cube = random.randint(1, 3)
        if life_cube == 1:
            self.to_study()
        elif life_cube == 2:
            self.to_sleep()
        elif life_cube == 3:
            self.to_chill()
        self.end_of_day()
nick = Student(name="Nick")
for day in range(365):
    if nick.alive == False:
        break
    nick.life(day)
