def has_subpattern(string):
    return (string * 2).find(string, 1) != len(string)
