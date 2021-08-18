def generate_hashtag(s):
    s = s.split()
    if len(s) > 140 or not (s):
        return False
    ans = '
    for word in s:
        ans += word.title()
    if len(ans) > 140 or not (s):
        return False
    return ans
