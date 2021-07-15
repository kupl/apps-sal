def stringify(list_):
    try:
        return '{} -> {}'.format(list_.data, stringify(list_.next))
    except AttributeError:
        return 'None'
