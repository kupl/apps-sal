class HTMLGen:

    def __init__(self):
        tags = ['a', 'b', 'p', 'body', 'div', 'span', 'title', 'comment']
        for tag in tags:
            setattr(self, tag, lambda content, tag=tag: '<' + tag + '>' + content + '</' + tag + '>' if not tag == 'comment' else '<!--' + content + '-->')
