class Dog ():
  def __init__(self, breed:str):
    self.breed = breed
  
  def bark(self) ->str:
      return "Woof"

snoopy = Dog("Beagle")
scoobydoo = Dog("Great Dane")
