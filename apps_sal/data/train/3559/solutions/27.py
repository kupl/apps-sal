def chromosome_check(sperm):
    sex = ["Congratulations! You're going to have a daughter.", "Congratulations! You're going to have a son."]
    return sex['Y' in sperm]
