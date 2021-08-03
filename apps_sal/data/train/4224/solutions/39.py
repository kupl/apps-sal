def dont_give_me_five(start, end):
    return len([n for n in range(start, end + 1) if not ((n % 5 == 0) & (n % 2 != 0)) | (n in range(50, 60)) | (n in range(150, 160))])
