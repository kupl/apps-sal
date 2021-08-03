def greet(name):
    name = name.lower()  # Converts all letters to lowercase
    for i in name:  # Loops through each letter in the given word
        o = name[0].upper() + name[1:]  # Converts first letter to uppercase
    return f"Hello {o}!"
