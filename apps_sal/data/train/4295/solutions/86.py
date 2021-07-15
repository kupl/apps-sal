def balanced_num(number):
    sum_left, sum_right=0, 0
    if len(str(number))%2==0:
        left=str(number)[:(len(str(number))//2)-1]
    else:
        left=str(number)[:len(str(number))//2]
    right=str(number)[(len(str(number))//2)+1:]
    for elem in left:
        sum_left+=int(elem)
    for elem in right:
        sum_right+=int(elem)
    if sum_left==sum_right:
        return 'Balanced'
    else:
        return 'Not Balanced'
