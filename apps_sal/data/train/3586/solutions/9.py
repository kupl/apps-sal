def html(tag, *contents, **attr):
    open_tag = tag + ''.join((f''' {('class' if n == 'cls' else n)}="{v}"''' for (n, v) in attr.items()))
    return '\n'.join((f'<{open_tag}>{c}</{tag}>' for c in contents)) or f'<{open_tag} />'
