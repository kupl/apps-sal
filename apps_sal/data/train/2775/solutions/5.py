def likes(names):
    """Convert list of names into strings of likes

    Args:
        names (list): List of string names

    Returns:
        str

    Examples:
        >>> likes(['Pavel', 'Yury', 'Sveta'])
        'Pavel, Yury and Sveta like this'
    """
    if not names:
        return 'no one likes this'
    if len(names) == 1:
        first = ''
        second = names[0]
    elif len(names) == 2:
        first = names[0]
        second = names[1]
    elif len(names) == 3:
        first = ', '.join(names[:2])
        second = names[-1]
    else:
        first = ', '.join(names[:2])
        second = '%d others' % (len(names) - 2)
    if first:
        return first + ' and ' + second + ' like this'
    else:
        return second + ' likes this'
