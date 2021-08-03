# cook your dish here
for _ in range(int(input())):
    name = input().split()

    if len(name) == 3:
        print((name[0])[0].upper(), '.', sep="", end=" ")
        print((name[1])[0].upper(), '.', sep="", end=" ")
        print(name[2].capitalize())

    elif len(name) == 2:
        print((name[0])[0].upper(), '.', sep="", end=" ")
        print(name[1].capitalize())

    else:
        print(name[0].capitalize())
