class Cat(Animal):

    def __init__(self, words):
        self.words = words

    def speak(self):
        return self.words + ' meows.'
