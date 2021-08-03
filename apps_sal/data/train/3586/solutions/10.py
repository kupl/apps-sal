def html(*args, **kwargs):
    attributes = tuple(f'{name.replace("cls", "class")}="{value}"' for name, value in kwargs.items())
    if len(args) == 1:
        return f'<{" ".join(args + attributes)} />'
    return '\n'.join(f'<{" ".join(args[:1] + attributes)}>{content}</{args[0]}>' for content in args[1:])
