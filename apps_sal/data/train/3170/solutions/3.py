def longer(s): #or    longer = lambda s:   if you're more daring :D
    return " ".join(sorted(s.split(" "),key=lambda x:(len(x),x)))
