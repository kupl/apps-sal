def greet(language):
    # store the data in a dictionary variable
    mylist = {'english': 'Welcome','czech': 'Vitejte','danish': 'Velkomst','dutch': 'Welkom','estonian': 'Tere tulemast','finnish': 'Tervetuloa','flemish': 'Welgekomen','french': 'Bienvenue','german': 'Willkommen','irish': 'Failte','italian': 'Benvenuto','latvian': 'Gaidits','lithuanian': 'Laukiamas','polish': 'Witamy','spanish': 'Bienvenido','swedish': 'Valkommen','welsh': 'Croeso'}
    # check if the input matches the key in myList
    if language in mylist:
        # if it matches print the value of the match
        return mylist[language]
    else:
        # if does not match just return English Value "Welcome" as the default
        return mylist['english']

