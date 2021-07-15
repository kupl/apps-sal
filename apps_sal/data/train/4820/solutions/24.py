class Cat(Animal):
    
    def __init__(self, text):
        self._text = text
        
    def speak(self):
        return f'{self._text} meows.'
