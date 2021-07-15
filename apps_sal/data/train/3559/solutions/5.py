def chromosome_check(sperm):
    return "Congratulations! You're going to have a {}.".format({"XY": "son", "XX": "daughter"}.get(sperm)) 
