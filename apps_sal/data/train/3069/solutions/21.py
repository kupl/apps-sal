def greet(language):
    try:
        d = {'english': 'Welcome', 'czech': 'Vitejte', 'danish': 'Velkomst', 'dutch': 'Welkom', 'estonian': 'Tere tulemast', 'finnish': 'Tervetuloa', 'flemish': 'Welgekomen', 'french': 'Bienvenue', 'german': 'Willkommen', 'irish': 'Failte', 'italian': 'Benvenuto', 'latvian': 'Gaidits', 'lithuanian': 'Laukiamas', 'polish': 'Witamy', 'spanish': 'Bienvenido', 'swedish': 'Valkommen', 'welsh': 'Croeso'}
        return d[language]
    except:
        return 'Welcome'
