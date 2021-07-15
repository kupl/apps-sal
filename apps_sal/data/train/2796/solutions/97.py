def areYouPlayingBanjo(name):
    plays = name[0].upper() == "R"
    answer = ["does not play", "plays"]
    return f"{name} {answer[plays]} banjo"
