def complete_binary_tree(a):
    arr1 = []
    for i in range(len(a) + 1):
        arr1.append(i)
    stack = []

    def inorder(arr, node):
        nonlocal stack
        if(node >= len(arr)):
            return
        inorder(arr, node * 2)
        stack.append(node)
        inorder(arr, node * 2 + 1)
    inorder(arr1, 1)

    result = [0 for row in range(len(a))]
    for i, lit in enumerate(result):
        result[i] = a[stack.index(i + 1)]
    return result
