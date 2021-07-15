def chromosome_check(sperm):
    if "XY" in sperm:
        return "Congratulations! You're going to have a son."
    elif "XX" in sperm:
        return "Congratulations! You're going to have a daughter."
