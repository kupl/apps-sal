def greet(language='english'):
    data={'english': 'Welcome',
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
    return data[language] if language in data else 'Welcome'
