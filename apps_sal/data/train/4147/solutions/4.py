def play_pass(s, n):
    return "".join([c.lower()
                    if (i % 2 != 0)
                    else c
                    for i, c in enumerate([chr((ord(c) - 65 + n) % 26 + 65)
                                          if (ord(c) in range(65, 91))
                                          else str(abs(int(c) - 9))
                                          if (ord(c) in range(48, 58))
                                          else c for c in s])][::-1])
