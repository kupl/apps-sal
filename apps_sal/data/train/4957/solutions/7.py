class Dog():
  def __init__(self, breed):
    self.breed = breed
    

snoopy = Dog("Beagle")

Dog.bark = lambda *args: "Woof"

scoobydoo = Dog("Great Dane")
