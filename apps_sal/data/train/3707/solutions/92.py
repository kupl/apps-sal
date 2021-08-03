class Book():
    def __init__(self, subject):
        self.subject = subject

    def __lt__(self, other):
        return self.subject.lower() < other.subject.lower()


def sorter(textbooks):
    a = [Book(subj) for subj in textbooks]
    a.sort()
    output = [i.subject for i in a]
    return output
