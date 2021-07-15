def greet_jedi(*args):
    return 'Greetings, master {1}{0}'.format(*(s.title()[:2+i] for i,s in enumerate(args)))

