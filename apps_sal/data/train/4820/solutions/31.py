class Cat(Animal):
    def __init__(self, name):
        self.name = name  # устанавливаем имя

    def speak(self):
        return (self.name + ' meows.')
