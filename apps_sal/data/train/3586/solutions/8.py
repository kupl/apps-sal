def html(tag, *content, **kwargs):
    # Format tag's attributes
    attributes = ''
    if kwargs:
        attribs = []
        for k, v in list(kwargs.items()):
            if k == 'cls':
                k = 'class'
            attribs.append(f'{k}="{v}"')
        attributes = ' ' + ' '.join(attribs)

    # Process content free tags
    if not content:
        return f'<{tag}{attributes} />'

    # Process content filled tags
    lines = []
    for line in content:
        lines.append(f'<{tag}{attributes}>{line}</{tag}>')
    return '\n'.join(lines)
