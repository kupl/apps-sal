def chromosome_check(sperm):
    gender = {"XY": "son", "XX": "daughter"}
    return f"Congratulations! You're going to have a {gender[sperm]}."
