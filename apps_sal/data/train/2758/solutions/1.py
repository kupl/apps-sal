def decode(number):
    split = str(number).replace('98', ' ').split()
    split[::2] = [''.join(chr(int(w[i: i + 3]) - 4)
                          for i in range(0, len(w), 3))
                  for w in split[::2]]
    split[1::2] = [str(int(n, 2)) for n in split[1::2]]
    return ', '.join(split)
