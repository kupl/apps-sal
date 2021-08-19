class Solution:

    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        if words == ['']:
            s = ' ' * maxWidth
            return [s]
        new = []
        for word in words:
            new.append([word, len(word)])
        res = []
        curr_length = 0
        start = 0
        print(new)
        for i in range(len(new)):
            if new[i][1] > maxWidth:
                return False
            elif curr_length + (i - start) + new[i][1] > maxWidth:
                if i - 1 - start == 0:
                    jiange = maxWidth - curr_length
                    s = ''
                    s += new[i - 1][0]
                    s += ' ' * (maxWidth - curr_length)
                    res.append(s)
                else:
                    if (maxWidth - curr_length) % (i - 1 - start) != 0:
                        jiange = (maxWidth - curr_length) // (i - 1 - start)
                        k = jiange
                        num = i - 2 - start
                        while num > 0:
                            if (maxWidth - curr_length - k) % num != 0:
                                k += jiange
                                num -= 1
                            else:
                                break
                    else:
                        k = 0
                        num = i - 1 - start
                        jiange = (maxWidth - curr_length) // (i - 1 - start)
                    s = ''
                    for j in range(start, i):
                        s += new[j][0]
                        if len(s) == maxWidth:
                            pass
                        elif jiange == 0:
                            pass
                        elif j < start + num:
                            s += ' ' * ((maxWidth - curr_length - k) // num)
                        else:
                            s += ' ' * jiange
                    res.append(s)
                start = i
                curr_length = new[i][1]
            else:
                curr_length += new[i][1]
        if start == len(new) - 1:
            jiange = maxWidth - new[-1][1]
            s = ''
            s += new[-1][0]
            s += ' ' * jiange
            res.append(s)
        else:
            i = len(new) - 1
            if i - start == 0:
                jiange = 0
            else:
                jiange = (maxWidth - curr_length) / (i - start) if (maxWidth - curr_length) % (i - start) == 0 else (maxWidth - curr_length) // (i - start)
            jiange = int(jiange)
            s = ''
            for j in range(start, i + 1):
                s += new[j][0]
                if len(s) == maxWidth:
                    pass
                elif j != i:
                    s += ' '
                else:
                    s += ' ' * (maxWidth - len(s))
            res.append(s)
        return res
