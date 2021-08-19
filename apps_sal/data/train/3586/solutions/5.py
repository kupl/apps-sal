def html(tag, *content, **attributes):
    attrib_str = ''.join((f''' {(key if key != 'cls' else 'class')}="{value}"''' for (key, value) in attributes.items()))
    if not content:
        return f'<{tag}{attrib_str} />'
    return '\n'.join((f'<{tag}{attrib_str}>{cnt}</{tag}>' for cnt in content))
