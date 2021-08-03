def greet(language='english'):
    # your code here

    dict_ = {'english': 'Welcome',
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

    return dict_[language] if language in dict_ else dict_['english']
