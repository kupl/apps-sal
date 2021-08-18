test = eval(input())
exer_book = []
min_stack = []
top = -1
for i in range(test):
    s = input().split()
    if(s[0] != "-1" and s[0] != "0"):
        n = int(s[0])
        if top >= 0 and n > exer_book[top][0]:
            min_stack[top] += 1
        else:
            exer_book.append((n, s[1]))
            min_stack.append(0)
            top += 1
    elif(s[0] == "-1"):
        print("%s %s" % (min_stack[top], exer_book[top][1]))
        exer_book.pop()
        min_stack.pop()
        top -= 1
