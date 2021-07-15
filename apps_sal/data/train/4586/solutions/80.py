keyboard="abcde123fghij456klmno789pqrst.@0uvwxyz_/"
def manhattan(x1, y1, x2, y2):
    return abs(y2 - y1) + abs(x2 - x1)
def index_2d(index_1d):
    return index_1d % 8, index_1d // 8
def tv_remote(word):
    c_x, c_y = 0, 0
    distance = 0
    for char in word:
        new_x, new_y = index_2d(keyboard.index(char))
        distance+= manhattan(c_x, c_y, new_x, new_y) + 1
        c_x, c_y = new_x, new_y
    return distance
