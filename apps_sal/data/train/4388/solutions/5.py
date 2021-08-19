def change_case(identifier, targetCase):
    # kebab make dashes after all capital, snake underscore after capital
    # camel makes kebab to caps
    # account for
    if isBad(identifier):
        return None
    if targetCase == 'snake':
        return snake(identifier)
    elif targetCase == 'camel':
        return camel(identifier)
    elif targetCase == 'kebab':
        return kebab(identifier)
    return None


def snake(myString):
    newString = myString
    for i in range(0, len(myString)):
        if ord(myString[i]) >= ord('A') and ord(myString[i]) <= ord('Z'):
            # means it is caps
            pos = newString.index(myString[i:])
            newString = newString[:pos] + '_' + newString[pos].lower() + newString[pos + 1:]
        elif myString[i] == '-':
            pos = newString.index(myString[i:])
            # newSting =
            newString = newString[:pos] + '_' + newString[pos + 1:]
    return newString.lower()


def kebab(myString):
    newString = myString
    for i in range(0, len(myString)):
        if ord(myString[i]) > ord('A') - 1 and ord(myString[i]) < ord('Z') + 1:
            # means it is caps
            pos = newString.index(myString[i:])
            newString = newString[:pos] + '-' + newString[pos].lower() + newString[pos + 1:]

        if myString[i] == '_':
            pos = newString.index(myString[i:])
            # newSting =
            newString = newString[:pos] + '-' + newString[pos + 1:]
        # means it is underscore
    return newString.lower()


def camel(myString):
    # why doesnt this work
    if len(myString) == 0:
        return myString
    myString = myString.replace('-', '_')
    newString = myString.split('_')
    for i in range(0, len(newString)):
        if i != 0:
            newString[i] = newString[i][0].upper() + newString[i][1:]
    return "".join(newString)
   #


def isBad(myString):
    if '_' in myString and '-' in myString:
        return True
    if '--' in myString or '__' in myString:
        return True
    if not myString.lower() == myString and '_' in myString:
        return True
    if not myString.lower() == myString and '-' in myString:
        return True
    return False
