def make_move(layout, start, end):
    x = [x for x in layout if start in x][0]
    index = (layout.index(x), x.index(start))
    y = [y for y in layout if end in y][0]
    index2 = (layout.index(y), y.index(end))
    move = abs(index[0] - index2[0]) + abs(index[1] - index2[1])
    return move + 1

def tv_remote(word):
    count = 0
    word = 'a' + word
    layout = [['a', 'b', 'c', 'd', 'e', '1', '2', '3'], ['f', 'g', 'h', 'i', 'j', '4', '5', '6'],
              ['k', 'l', 'm', 'n', 'o', '7', '8', '9'], ['p', 'q', 'r', 's', 't', '.', '@', '0'],
              ['u', 'v', 'w', 'x', 'y', 'z', '_', '/']]
    for i in range(len(word)-1):
        count += make_move(layout, word[i], word[i+1])
    return count
