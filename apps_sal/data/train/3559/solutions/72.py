def chromosome_check(sperm):
    if sperm == "XX":
        return "Congratulations! You're going to have a daughter."
    if sperm == "XY" or "YX":
        return "Congratulations! You're going to have a son."
