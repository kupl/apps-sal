def stringify(head):
    if head is None:
        return "None"
    return "{} -> {}".format(head.data, stringify(head.__next__))
