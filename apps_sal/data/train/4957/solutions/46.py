class Dog ():
  def __init__(self, breed):
    self.breed = breed
  def bark(self): 
      return "Woof"

# Instantiate two Dog Objects
snoopy = Dog("Beagle")
scoobydoo = Dog("Great Dane")

# Call bark() method
snoopy.bark()
scoobydoo.bark()
