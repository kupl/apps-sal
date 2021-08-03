def solve(s):
    # assumes no negatives, per problem statement
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    ans = ""

    for char in s:
        if char in alphabet:
            ans += " "
        else:
            ans += char
    ans = ans.split(" ")

    return max(int(x) for x in ans if x)  # 0 will eval false
