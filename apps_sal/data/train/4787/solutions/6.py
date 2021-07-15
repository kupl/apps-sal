def remove(s):
    n = s.count("!")
    return s.replace("!", "") + "!" * n
