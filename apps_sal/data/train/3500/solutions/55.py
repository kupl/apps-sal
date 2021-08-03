def remove_exclamation_marks(s):
    for i in range(len(s)):
        count = s.count("!")
        s = s.replace('!', '', count)
    return s
