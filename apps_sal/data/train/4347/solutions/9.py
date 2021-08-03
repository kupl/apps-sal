def are_equally_strong(your_left, your_right, friends_left, friends_right):

    m = (your_left + your_right)

    f = (friends_left + friends_right)

    if your_left == friends_left and your_right == friends_right or your_left == friends_right and your_right == friends_left:

        return True

    else:

        return False
