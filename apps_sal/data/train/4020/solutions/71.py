def validate_hello(greetings):
    saludos = ["hello","ciao","salut","hallo","hola","ahoj","czesc"]
    for saludo in saludos:
        if saludo in greetings.lower():
            return True
    return False

