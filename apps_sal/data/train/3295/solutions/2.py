def split_in_parts(s, part_length): 
    new = ""
    i = 0
    for x in s:                   # Recorremos s
        if i == part_length:      # Si toca meter un espacio...
            new += " "            # Lo hacemos
            new += x              # Y añadimos la siguiente letra porque sino el ciclo se salta algunas
            i = 1
        else:                     # Si no toca meter un espacio...
            new += x              # Añadimos la letra y punto
            i += 1
    return new
