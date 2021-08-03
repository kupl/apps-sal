for _ in range(int(input())):
    st = input().strip()
    an = 0
    for ch in st:
        if ch == "4" or ch == "7":
            continue
        else:
            an += 1
    print(an)
