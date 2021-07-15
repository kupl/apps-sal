def get_strings(city):
    soln = []
    used = ''
    for letter in city.lower():
        if letter in used or letter == ' ':
            continue
        else:
            solnstring = ''
            solnstring += letter + ':'
            for x in range(city.lower().count(letter)):
                solnstring += '*'
            soln.append(solnstring)
            used += letter
    return ','.join(soln)
