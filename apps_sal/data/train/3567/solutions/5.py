def leo(oscar):
    r = ["Leo finally won the oscar! Leo is happy",
        "Not even for Wolf of wallstreet?!",
        "When will you give Leo an Oscar?",
        "Leo got one already!"]
    return r[0] if oscar==88 else r[1] if oscar==86 else r[2] if oscar==87 or oscar<86 else r[3]
