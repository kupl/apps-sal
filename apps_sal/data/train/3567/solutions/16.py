def leo(oscar: int) -> str:
    """ Will oscar go to Leonardo DiCaprio? """
    return {oscar == 88: 'Leo finally won the oscar! Leo is happy', oscar == 86: 'Not even for Wolf of wallstreet?!', oscar not in (86, 88) and oscar <= 87: 'When will you give Leo an Oscar?', oscar > 88: 'Leo got one already!'}.get(True)
