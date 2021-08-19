def greet(language):
    dict = {'english': 'Welcome',
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
    if language not in dict:
        return dict["english"]
    else:
        return dict[language]
    # your code here
