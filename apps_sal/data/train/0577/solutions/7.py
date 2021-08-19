# book = ''.join(sorted(str(raw_input())))
book = input()


for i in range(0, int(input())):
    words = str(input())
    check = 0
    for letter in sorted(words):
        if letter in book:
            check = check + 1

    if check == len(words):
        print("Yes")
    else:
        print("No")
