def stringify(node):
    if node == None:
        return 'None'
    returnString = ''
    while node != None:
        returnString += str(node.data) + ' -> '
        node = node.next
    returnString += 'None'
    return returnString
