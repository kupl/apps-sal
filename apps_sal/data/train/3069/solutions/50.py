def greet(language):
    welcome_messages = {'english': 'Welcome', 'czech': 'Vitejte', 'danish': 'Velkomst', 'dutch': 'Welkom', 'estonian': 'Tere tulemast', 'finnish': 'Tervetuloa', 'flemish': 'Welgekomen', 'french': 'Bienvenue', 'german': 'Willkommen', 'irish': 'Failte', 'italian': 'Benvenuto', 'latvian': 'Gaidits', 'lithuanian': 'Laukiamas', 'polish': 'Witamy', 'spanish': 'Bienvenido', 'swedish': 'Valkommen', 'welsh': 'Croeso'}
    return welcome_messages[language] if language in welcome_messages else 'Welcome'
