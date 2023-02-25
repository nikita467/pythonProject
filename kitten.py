class animals:
    def breathe(self):
        pass

    def walk(self):
        pass

    def eat(self):
        pass


class kitten(animals):
    def drink_milk(self):
        pass

class kitten(animals):
  def drink_milk(self):
    print('drinking a milk')
  def eat(self):
    self.walk()
    print('Im eating')
    self.drink_milk()


class kitten:
    def __init__(self, brown):
        self.color = brown


bobik= kitten('brown')
print(bobik.color)
