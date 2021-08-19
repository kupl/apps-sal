def html(tag, *content, **kwargs):
    attributes = ''
    if kwargs:
        attribs = []
        for (k, v) in list(kwargs.items()):
            if k == 'cls':
                k = 'class'
            attribs.append(f'{k}="{v}"')
        attributes = ' ' + ' '.join(attribs)
    if not content:
        return f'<{tag}{attributes} />'
    lines = []
    for line in content:
        lines.append(f'<{tag}{attributes}>{line}</{tag}>')
    return '\n'.join(lines)
