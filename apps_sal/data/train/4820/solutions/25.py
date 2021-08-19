class Cat(Animal):

    def __init__(self, word):
        self.word = word
        return

    def speak(self):
        return self.word + ' meows.'
