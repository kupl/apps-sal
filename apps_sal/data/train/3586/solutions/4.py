ALIAS = {'cls': 'class'}


def html(tag, *contents, **attribs):
    attrib_repr = ' ' + ' '.join((f'{ALIAS.get(key, key)}="{value}"' for (key, value) in attribs.items())) if attribs else ''
    if not contents:
        return f'<{tag}{attrib_repr} />'
    return '\n'.join((f'<{tag}{attrib_repr}>{content}</{tag}>' for content in contents))
