class HTMLGen:
    def __init__(self):
        self.a = lambda t: self.tag("a", t)
        self.b = lambda t: self.tag("b", t)
        self.p = lambda t: self.tag("p", t)
        self.body = lambda t: self.tag("body", t)
        self.div = lambda t: self.tag("div", t)
        self.span = lambda t: self.tag("span", t)
        self.title = lambda t: self.tag("title", t)

    def tag(self, tag_str, content):
        return "<{}>{}</{}>".format(tag_str, content, tag_str)

    def comment(self, content):
        return "<!--{}-->".format(content)
