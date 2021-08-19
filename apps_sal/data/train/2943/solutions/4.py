def complete_binary_tree(a):
    arr1 = []  # 기본 node들이 차례대로 있는 배열
    for i in range(len(a) + 1):  # 개수만큼 +1을 해줌. 0부터 시작하게 하기 위함
        arr1.append(i)
    stack = []  # inorder 순서를 나타낼 배열

    def inorder(arr, node):  # inorder라는 함수는 arr와 node값을 input으로 받음
        nonlocal stack  # 함수 내의 함수에서 부르므로 nonlocal을 사용하여 내부수정이 밖에도 영향을 미치도록 함.
        if(node >= len(arr)):
            return
        inorder(arr, node * 2)
        stack.append(node)
        inorder(arr, node * 2 + 1)
    inorder(arr1, 1)  # 1부터하여 inorder 순서를 따냄. stack에 저장됨

    result = [0 for row in range(len(a))]  # result를 저장할 배열을 선언함.
    for i, lit in enumerate(result):
        result[i] = a[stack.index(i + 1)]  # 알맞는 값으로 바꿔줌
    return result
