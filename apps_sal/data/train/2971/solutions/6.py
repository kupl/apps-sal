def watch_pyramid_from_the_side(characters=None):
    """Display from the pyramid from the side"""
    if characters is None:
        return None
    elif characters == '':
        return ''
    characters = characters[::-1]
    length = len(characters)
    output = []
    num = 1
    for i in range(len(characters)):
        output.append((length - i - 1) * ' ' + num * characters[i] + (length - i - 1) * ' ')
        num += 2
    return '\n'.join(output)


def watch_pyramid_from_above(characters=None):
    """Print the pyramid from the side."""
    if characters is None:
        return None
    elif characters == '':
        return ''
    size = len(characters)
    output = []
    for i in range(size):
        output.append(characters[:i] + characters[i] * (size - 1 - i) + characters[i])
    output.extend(output[:-1][::-1])
    return '\n'.join([row + row[:-1][::-1] for row in output])


def count_visible_characters_of_the_pyramid(characters=None):
    """Return the count of letters visible on the pyramid."""
    if not characters:
        return -1
    return (len(characters) * 2 - 1) ** 2


def count_all_characters_of_the_pyramid(characters=None):
    """Return the count of letters used in the pyramid."""
    if not characters:
        return -1
    return sum([(2 * num + 1) ** 2 for num in range(len(characters))])
