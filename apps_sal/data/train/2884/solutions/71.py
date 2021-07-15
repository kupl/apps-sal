def stringify(node):
    if not node:
        return 'None'
    ans = []
    while node:
        ans.append(str(node.data))
        node = node.next
    return ' -> '.join(ans) + ' -> None'
