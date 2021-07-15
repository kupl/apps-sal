KEYBOARD_STRING = "a    b   c   d   e   1   2   3 \
                    f   g   h   i   j   4   5   6 \
                    k   l   m   n   o   7   8   9 \
                    p   q   r   s   t   .   @   0 \
                    u   v   w   x   y   z   _   /"

keyboard_list = list(KEYBOARD_STRING.split())

keyboard_dictionary = {}

n = 0
for i in keyboard_list:
    row = n // 8
    col = (n + 8) % 8
    keyboard_dictionary[i] = [row, col]
    n += 1

def tv_remote(word):
    word_list = list(word)
    count = 0
    row = 0
    col = 0
    for i in word_list:
        col_dist = abs(col - keyboard_dictionary[i][1])
        row_dist = abs(row - keyboard_dictionary[i][0])
        col = keyboard_dictionary[i][1]
        row = keyboard_dictionary[i][0]
        count += col_dist + row_dist + 1
    return count
