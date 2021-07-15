class Dog ():
  def __init__(self, breed):
    self.breed = breed
    
  def bark(self):
      if self.breed == 'Beagle' or self.breed == "Great Dane":
          return "Woof"
      else:
          return "undefined"
    

snoopy = Dog("Beagle")
scoobydoo = Dog("Great Dane")
