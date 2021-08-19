class Student:

    def __init__(self, name, fives, tens, twenties):
        self.name = name
        self.fives = fives
        self.tens = tens
        self.twenties = twenties


phil = Student('Phil', 2, 2, 1)
cam = Student('Cameron', 2, 2, 0)
geoff = Student('Geoff', 0, 3, 0)


def most_money(students):
    hajs = [stud.fives * 5 + stud.tens * 10 + stud.twenties * 20 for stud in students]
    return students[hajs.index(max(hajs))].name if hajs.count(max(hajs)) == 1 else 'all'
