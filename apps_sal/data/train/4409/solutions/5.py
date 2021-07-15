def noonerize(numbers):
    nb1, nb2 = map(str, numbers)
    try:
        return abs(int(nb2[0] + nb1[1:]) - int(nb1[0] + nb2[1:]))
    except ValueError:
        return "invalid array"
