def areYouPlayingBanjo(name):
    for i in name:
        if i =='R' or i=='r':
            return name+ " "+"plays banjo"
        else:
            return name+" does not play banjo"
