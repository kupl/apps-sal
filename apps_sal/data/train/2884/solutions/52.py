def stringify(node):
    ans = []
    while node:
        ans.append(str(node.data))
        node = node.__next__
    ans.append('None')
    return ' -> '.join(ans)
