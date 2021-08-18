
def stringify_attrs(attrs):
    result = ''
    for attr in attrs:
        new_attr = attrs[attr]
        if attr == 'cls':
            attr = 'class'
        result += attr + '=' + '"' + new_attr + '"' + ' '
    if not result:
        return ''
    return ' ' + result.strip()


def html(tag, *bodies, **attrs):
    if not bodies:
        result = '<' + tag + stringify_attrs(attrs) + ' />'
        return result
    result = ''
    for body in bodies:
        result += '<' + tag + stringify_attrs(attrs) + '>' + body + '</' + tag + '>' + '\n'
    return result.strip()
