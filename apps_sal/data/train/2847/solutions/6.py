def greet_jedi(first, last):
    # Your code goes here.
    one = last[0:3].capitalize()
    two = first[0:2].capitalize()
    return ("Greetings, master {}{}".format(one, two))
