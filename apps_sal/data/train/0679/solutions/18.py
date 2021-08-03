import sys

n = int(sys.stdin.readline())
book_stack = [[999999, 'NAME', 0]]
length = 0

while n:
    inp = sys.stdin.readline().strip()

    if inp == '-1':
        print(str(book_stack[length][2]) + ' ' + book_stack[length][1])
        del book_stack[length]
        length -= 1

    else:
        value, name = inp.split()
        value = int(value)

        if value != 0:
            if value > book_stack[length][0]:
                book_stack[length][2] += 1
            else:
                book_stack.append([value, name, 0])
                length += 1

    n -= 1
