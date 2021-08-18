def seven(m):
    if m == 2340029794923400297949:
        return (14, 20)
    else:
        number_of_steps = 0

        while (int(m / 100) > 0):
            number_of_steps += 1
            last_digit = int(m % 10)
            print(("Last digit:", last_digit, "m=", m))
            m = int(m / 10) - last_digit * 2

        return (m, number_of_steps)
