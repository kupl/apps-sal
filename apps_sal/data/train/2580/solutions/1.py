def __starting_point():
    string = input().strip()
    print(*sorted(string, key=lambda x: (-x.islower(), x.isdigit() - x.isupper(), x in '02468', x)), sep='')


__starting_point()
