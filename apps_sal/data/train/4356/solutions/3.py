REGEX = __import__("re").compile(
    r"(.).*\1"  # Duplicate digit
    r"|[01].+|.+[01]"  # 0 or 1 and another digit
    r"|(23|32).*6|6.*(23|32)"  # 2*3 and a 6 before or after
    r"|(24|42).*8|8.*(24|42)"  # 2*4 and a 8 before or after
    r"|(26|62).*(34|43)|(34|43).*(26|62)"  # 2*6 and 3*4 before or after
    r"|(29|92).*(36|63)|(36|63).*(29|92)"  # 2*9 and 3*6 before or after
    r"|(38|83).*(46|64)|(46|64).*(38|83)"  # 3*8 and 4*6 before or after
    r"|(49|94).*(236|263|326|362|623|632)|(236|263|326|362|623|632).*(49|94)"  # 4*9 and 2*3*6 before or after
    r"|(89|98).*(346|364|436|463|634|643)|(346|364|436|463|634|643).*(89|98)"  # 8*9 and 3*4*6 before or after
).search


def colorful(number):
    return not REGEX(str(number))
