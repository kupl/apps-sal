def chromosome_check(sperm):
    gender = 'son' if 'Y' in sperm else 'daughter'
    return f"Congratulations! You're going to have a {gender}."
