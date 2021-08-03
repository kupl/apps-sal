def change_case(identifier, targetCase):
    id = list(str(identifier))
    conv = []

    if identifier.islower() == False and (id.count('-') != 0 or id.count('_') != 0) == True:  # checks if there are upper case and hyphens or underscores
        return None

    if id.count('-') != 0 and id.count('_') != 0:
        return None

    if targetCase == 'snake':
        return change_snake(id, conv)

    if targetCase == 'camel':
        return change_camel(id, conv)

    if targetCase == 'kebab':
        return change_kebab(id, conv)

    else:
        return None


def change_snake(id, conv):  # converts Capital to _lower
    for i in id:
        if i.isupper() == True:
            conv.append('_' + i.lower())
            # conv.append(i.lower())

        elif i == '-':
            conv.append('_')

        else:
            conv.append(i)

    return ''.join(conv)


def change_camel(id, conv):  # converts -lower to Capital
    ids = id.copy()
    ids.insert(0, '.')
    n = 0

    for i in id:
        n = n + 1

        if i == '-' or i == '_':
            continue

        if ids[n - 1] == '-' or ids[n - 1] == '_':

            conv.append(i.upper())

        else:
            conv.append(i)

    return ''.join(conv)


def change_kebab(id, conv):  # converts
    for i in id:
        if i == '_':
            conv.append('-')
            continue

        if i.isupper() == True:
            conv.append('-' + i.lower())

        else:
            conv.append(i)

    return ''.join(conv)
