class Circle(object):
    def __init__(self, items):
        self.items = items[:]

    def pop(self, index):
        norm_index = index % len(self.items)
        return self.items.pop(norm_index), norm_index

    def not_empty(self):
        return self.items


def josephus_iter(items, k):
    circle = Circle(items)
    i = k - 1  # index 0-based
    while circle.not_empty():
        item, i = circle.pop(i)
        yield item
        i += k - 1


def josephus(items, k):
    return list(josephus_iter(items, k))
