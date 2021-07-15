def stringify(node):
    then_case = ''
    result = ''
    while node!=None:
        then_case = node.data
        node = node.next
        result+=str(then_case)+' -> '
    return result+'None'
