def tv_remote(word):
    letters = 'abcde123fghij456klmno789pqrst.@0uvwxyz_/'
    steps = 0
    (x, y) = (0, 0)
    for i in word:
        (x1, y1) = (letters.find(i) % 8, letters.find(i) // 8)
        steps += abs(x - x1) + abs(y - y1) + 1
        (x, y) = (x1, y1)
    return steps
