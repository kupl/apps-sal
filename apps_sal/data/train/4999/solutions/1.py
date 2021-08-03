def capital(capitals):
    ans = []
    for each in capitals:
        a = each.get('state', '')
        b = each.get('country', '')
        c = each.get('capital')
        ans.append('The capital of {}{} is {}'.format(a, b, c))
    return ans
