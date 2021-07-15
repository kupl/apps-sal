def to_camel_case(text):
    words = text.replace('_', '-').split('-')
    return words[0] + ''.join([x.title() for x in words[1:]])
