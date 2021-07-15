def leo(oscar):
    return  ("Leo got one already!",
             "When will you give Leo an Oscar?",
             "Not even for Wolf of wallstreet?!",
             "Leo finally won the oscar! Leo is happy")[(oscar == 86) + (oscar < 88) + 3 * (oscar == 88)]
