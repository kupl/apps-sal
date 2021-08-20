def palindrome(num):
    l = list(str(num))
    if len(l) == 1:
        return num
    else:
        l2 = [x for x in l if l.count(x) >= 2]
        l22 = list(set(l2))
        l1 = [x for x in list(set(l)) if l.count(x) % 2 != 0]
        l22.sort()
        if len(l2) == 0 and len(l1) > 0 or len(l2) == l2.count('0'):
            return int(max(l1))
        else:
            l2a = ''
            for i in range(len(l22)):
                if l2.count(l22[i]) % 2 > 0:
                    n = l2.count(l22[i]) // 2
                else:
                    n = l2.count(l22[i]) / 2
                l2a = l2a + l22[i] * int(n)
            l2b = l2a[::-1]
            if len(l1) > 0:
                l2c = l2b + str(max(l1)) + l2a
            else:
                l2c = l2b + l2a
            return int(l2c)


def product1(list, pro, i, out):
    if i < len(list):
        proa = pro
        prob = list[i]
        pro = proa * prob
        if pro not in out:
            out.append(pro)
        product1(list, pro, i + 1, out)
        product1(list, proa, i + 1, out)
        product1(list, prob, i + 1, out)


def numeric_palindrome(*args):
    args1 = [x for x in args if x > 1]
    args1.sort()
    out1 = []
    pro1 = []
    if args1 == [] and args.count(1) > 1:
        return 1
    elif args.count(0) == len(args) - 1 or args1 == []:
        return 0
    elif len(args1) == 1:
        return palindrome(args1[0])
    else:
        product1(args1, args1[0], 1, pro1)
        if args.count(1) > 0:
            pro1 = pro1 + args1
        for j in pro1:
            out = palindrome(j)
            out1.append(out)
    return max(out1)
