N = "A A# B C C# D D# E F # F# G G#".split()
get_note = g = lambda n: 12 < n // 1 < 27 and N[int(n) - 13] or g(n / 2)
