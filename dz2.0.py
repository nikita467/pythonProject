import random
class cat:
    def __init__(self,name):
        self.name = name
        self.gladness = 20
        self.progress = 0
        self.alive = True


    def to_eat(self):
        print("I need eat!")
        self.progress += 4
        self.gladness -= 1
    def to_poop(self):
        print("Im go to WC")
        self.progress -= 5
        self.gladness += 2

    def to_sleep(self):
        print("I will sleep")
        self.gladness += 4


    def to_walk(self):
        print("Go walk")
        self.gladness += 4
        self.progress -= 3

    def to_play(self):
        print("Lets go play with me")
        self.gladness += 4
        self.progress -= 2

    def end_of_day(self):
        print(f"Gladness = {self.gladness}")
        print(f"Progress = {round(self.progress, 2)}")
    def life(self, day):
        day = "Day" + str(day) + "of" + self.name + "life"
        print(f"{day:=^50}")
        life_cube = random.randint(1, 3)
        if life_cube == 1:
            self.to_play()
        elif life_cube == 2:
            self.to_sleep()
        elif life_cube == 3:
            self.to_eat()
        self.end_of_day()
nick = cat(name="Caisy")
for day in range(365):
    if nick.alive == False:
        break
    nick.life(day)