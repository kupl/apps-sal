def word_square(letters):
    root = int(len(letters)**0.5)
    return len(letters)**0.5 == root and sum([ letters.count(i)%2 for i in set(letters) ]) <= root
