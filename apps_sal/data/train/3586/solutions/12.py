def html(*args, **kwargs):
    keywords, elements = [], []
    if kwargs:
        for key, value in kwargs.items():
            if key == "cls":
                key = 'class'
            keywords.append(f'{key}="{value}"')
    if len(args) == 1:
        if kwargs:
            element = f'<{args[0]}'
            for key in keywords:
                element += ' ' + key
            element += ' />'
            return element
        else:
            return f'<{args[0]} />'
    for i, arg in enumerate(args):
        if i == 0:
            tag = arg
        else:
            element = f'<{tag}'
            if kwargs:
                for key in keywords:
                    element += ' ' + key
            element += f'>{arg}</{tag}>'
            elements.append(element)
    return "\n".join(element for element in elements)
