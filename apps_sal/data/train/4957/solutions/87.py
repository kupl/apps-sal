class Dog ():
  def __init__(self, breed, sound="Woof"):
    self.breed = breed
    self.sound = sound
    
  def bark(self):
    return self.sound
    
    

snoopy = Dog("Beagle")

snoopy.bark = lambda: "Woof"

scoobydoo = Dog("Great Dane")
