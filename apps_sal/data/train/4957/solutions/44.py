class Dog ():
  def __init__(self, breed):
    self.breed = breed
    
  def bark(cls):
      return "Woof"
    

snoopy = Dog("Beagle")

snoopy.bark = lambda: "Woof"

scoobydoo = Dog("Great Dane")
