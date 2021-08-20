def html(tag, *content, **attributes):
    attrs = ''.join((f''' {('class' if name == 'cls' else name)}="{value}"''' for (name, value) in attributes.items()))
    return '\n'.join((f'<{tag}{attrs}>{element}</{tag}>' for element in content)) if content else f'<{tag}{attrs} />'
