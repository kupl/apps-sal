for _ in range(int(input())):
    name = input().split()

    if len(name) == 3:
        print(f"{name[0][0].upper()}. {name[1][0].upper()}. {name[2].title()}")
    elif len(name) == 2:
        print(f"{name[0][0].upper()}. {name[1].title()}")
    else:
        print(name[0].title())
