def elevator(left, right, call):
    return 'left' if left == call and left != right or left > right and call > left or right > left and call < left else 'right'
