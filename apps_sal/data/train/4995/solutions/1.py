class Tag:

    def __init__(self, name):
        self.template = '<{0}>{{}}</{0}>'.format(name) if name != 'comment' else '<!--{}-->'
      
    __call__ = lambda self, content: self.template.format(content)


class HTMLGen:
    __getattr__ = lambda self, name: Tag(name)
