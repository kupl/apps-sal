def __starting_point():
    s = input()

    print((any(char.isalnum() for char in s)))
    print((any(char.isalpha() for char in s)))
    print((any(char.isdigit() for char in s)))
    print((any(char.islower() for char in s)))
    print((any(char.isupper() for char in s)))


__starting_point()
