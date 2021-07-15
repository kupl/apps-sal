class Dog ():
  def __init__(self, breed):
    self.breed = breed
  def bark(self, bark='Woof'):
      return bark

    

snoopy = Dog("Beagle")

snoopy.bark = lambda: "Woof"

scoobydoo = Dog("Great Dane")
