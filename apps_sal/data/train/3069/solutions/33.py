def greet(language):

    dict_lang = {'english': 'Welcome',
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
                 'welsh': 'Croeso'
                 }
    dict_lang.setdefault(language, 'Welcome')
    return dict_lang[language]
