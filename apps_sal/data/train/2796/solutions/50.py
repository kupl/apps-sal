def areYouPlayingBanjo(name):
    # Implement me!
    if name[0] == 'R' or name[0] == "r":
        output = (name + " plays banjo")
    else:
        output = (name + " does not play banjo")
    return output


user_name = "ralan"

print(areYouPlayingBanjo(user_name))
