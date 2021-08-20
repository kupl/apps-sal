stringify = lambda node, s='': stringify(node.next, s + f'{node.data} -> ') if node else s + 'None'
