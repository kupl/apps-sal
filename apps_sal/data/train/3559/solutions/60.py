def chromosome_check(sperm):
    return "Congratulations! You\'re going to have a {}.".format(["son", "daughter"][sperm.count("X") - 1])
