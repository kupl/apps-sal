class Dog ():
  def __init__(self, breed):
    self.breed = breed
    

snoopy = Dog("Woof")

snoopy.bark = lambda: "Woof"

scoobydoo = Dog("Woof")

scoobydoo.bark = lambda: "Woof"
