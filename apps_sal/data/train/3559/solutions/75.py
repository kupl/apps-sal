def chromosome_check(sperm):
    gender = {"XX": "daughter", "XY": "son"}
    return f"Congratulations! You\'re going to have a {gender[sperm]}."
