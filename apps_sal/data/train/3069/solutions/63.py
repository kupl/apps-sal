def greet(language):
    lang_greet = {'english': 'Welcome',
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
    return lang_greet[language] if language in lang_greet else lang_greet['english']
