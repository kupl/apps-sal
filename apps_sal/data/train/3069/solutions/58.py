GREETINGS = {'english': 'Welcome',
'czech': 'Vitejte',
'danish': 'Velkomst',
'dutch': 'Welkom',
'estonian': 'Tere tulemast',
'finnish': 'Tervetuloa',
'flemish': 'Welgekomen',
'french': 'Bienvenue',
'german': 'Willkommen',
'irish': 'Failte',
'italian': 'Benvenuto',
'latvian': 'Gaidits',
'lithuanian': 'Laukiamas',
'polish': 'Witamy',
'spanish': 'Bienvenido',
'swedish': 'Valkommen',
'welsh': 'Croeso'}

def greet(language):
    try: greeting = GREETINGS[language]
    except KeyError: greeting = 'Welcome'
    return greeting
