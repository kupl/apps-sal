def leo(oscar):
    """Return string describing Leo based on 'oscar'.

    (int) -> str

    Conditions:
        - If 'oscar' was 88, you should return "Leo finally won the oscar! Leo is happy",
        - If 'oscar' was 86, you should return "Not even for Wolf of wallstreet?!",
        - If 'oscar' was not 88 or 86 (and below 88) you should return "When will you give Leo an Oscar?",
        - If 'oscar' was over 88 you should return "Leo got one already!"

    >>> leo(88)
    "Leo finally won the oscar! Leo is happy"

    Example test cases:
        - test.assert_equals(leo(85),"When will you give Leo an Oscar?")
        - test.assert_equals(leo(86),"Not even for Wolf of wallstreet?!")
        - test.assert_equals(leo(87),"When will you give Leo an Oscar?")
        - test.assert_equals(leo(88),"Leo finally won the oscar! Leo is happy")
        - test.assert_equals(leo(89),"Leo got one already!")
    """
    if oscar > 88:
        return "Leo got one already!"
    elif oscar == 88:
        return "Leo finally won the oscar! Leo is happy"
    elif oscar == 86:
        return "Not even for Wolf of wallstreet?!"
    else:
        return "When will you give Leo an Oscar?"
