def sorter(textbooks):
    #Cramming before a test can't be that bad?
    def f(x):
        return x.lower()
    return sorted(textbooks,key=f)
