def super_pad(string, width, fill=" "):
    if fill == '':
        return string
    if width == 0:
        return ''
    diff = width-len(string)
    if diff <= 0:
        if fill[0] == '>':
            return string[:width]
        elif fill[0] == '^':
            a = abs(diff)//2
            b = abs(diff)-a
            if a == 0 and diff == -1:
                return string[:-1]
            return string[b:] + string[:-a]
        elif fill[0] == '<':
            fill = fill[1:]
        return string[-width:]
    else:
        if fill[0] == '>':
            fill = fill[1:]
            if len(fill) > diff:
                return string + fill[:diff]
            else:
                ans, i = '', 0
                while i < diff:
                    ans += fill
                    if len(ans) >= diff:
                        ans = ans[:diff]
                        break
                    i += 1
                return string + ans        
        elif fill[0] == '^':
            fill = fill[1:]
            a = diff//2
            b = diff-a
            if len(fill) > diff:
                return fill[:b] + string + fill[:a]
            else:
                ans1, i, ans2 = '', 0, ''
                while i < b:
                    ans1 += fill
                    ans2 += fill
                    if len(ans2) >= diff//2 :
                        ans1 = ans1[:a]
                        if len(ans1) >= diff-len(ans2):
                            ans2 = ans2[:b]
                            break
                    i += 1
                return ans2 + string + ans1
        elif fill[0] == '<':
            fill = fill[1:]
            if len(fill) > diff:
                return fill[:diff] + string
            else:
                ans, i = '', 0
                while i < diff:
                    ans += fill
                    if len(ans) >= diff:
                        ans = ans[:diff]
                        break
                    i += 1
                return ans + string
        else:
            if len(fill) > diff:
                return fill[:diff] + string
            else:
                ans, i = '', 0
                while i < diff:
                    ans += fill
                    if len(ans) >= diff:
                        ans = ans[:diff]
                        break
                    i += 1
                return ans + string
