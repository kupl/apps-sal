for _ in range(int(input())):
    s = list(input())
    letters = set()
    flag = False
    for letter in s:
        if letter not in letters:
            letters.add(letter)
        else:
            flag = True
            break

    if flag:
        print("yes")
    else:
        print("no")
