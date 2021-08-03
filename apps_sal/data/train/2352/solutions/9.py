def main():
    s = input()
    le = len(s)
    i = 3 + s.startswith("http")
    res = [s[:i] + ":/"]
    j = s.find("ru", i + 1)
    res.append(s[i:j] + ".ru")
    if j + 2 < le:
        res.append(s[j + 2:])
    print('/'.join(res))


def __starting_point():
    main()


__starting_point()
