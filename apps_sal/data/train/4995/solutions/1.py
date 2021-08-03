class Tag:

    def __init__(self, name):
        self.template = '<{0}>{{}}</{0}>'.format(name) if name != 'comment' else '<!--{}-->'

    def __call__(self, content): return self.template.format(content)


class HTMLGen:
    def __getattr__(self, name): return Tag(name)
