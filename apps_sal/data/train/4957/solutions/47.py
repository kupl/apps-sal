class Dog ():
  def __init__(self, breed):
    self.breed = breed
    

snoopy = Dog("Beagle")

snoopy.bark = lambda: "Woof"

Dog.bark = staticmethod(snoopy.bark)

scoobydoo = Dog("Great Dane")
