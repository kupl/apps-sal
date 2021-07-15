def html(*args, **k_args):
    attrs = []
    for k, v in list(k_args.items()):
        if k=='cls':
            k='class'
        attrs.append(k+'="'+v+'"')
    attrs = ' '.join(attrs)
    args = list(args)
    tag = args.pop(0)
    opentag=' '.join(['<'+tag, attrs]).strip()
    if len(args)==0:
        return opentag + ' />'
    return '\n'.join([opentag+'>'+txt+'</'+tag+'>' for txt in args])

