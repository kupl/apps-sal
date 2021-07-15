def count_deaf_rats(s):
    return s.replace(" ", "")[::2].count("O")
