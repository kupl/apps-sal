class Dog ():
  def __init__(self, breed):
    self.breed = breed
    
    

snoopy = Dog("Beagle")
scoobydoo = Dog("Great Dane")

snoopy.bark = lambda: "Woof"
scoobydoo.bark = lambda: "Woof"




snoopy.bark()
scoobydoo.bark()
