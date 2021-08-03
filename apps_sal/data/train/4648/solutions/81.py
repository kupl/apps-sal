def automorphic(n):
    squared_number = n ** 2
    if str(squared_number)[-len(str(n)):] == str(n):
        return "Automorphic"
    else:
        return "Not!!"
