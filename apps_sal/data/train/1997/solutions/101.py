class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        tree = {}
        for x, y in intervals:
            cursor = tree
            if not tree:
                tree['value'] = (x, y)
            else:
                while True:
                    if x < cursor['value'][0]:
                        tmp = cursor.get('left', {})
                        if tmp:
                            cursor = tmp
                        else:
                            cursor['left'] = {'value': (x, y)}
                            break
                    elif x > cursor['value'][0]:
                        tmp = cursor.get('right', {})
                        if tmp:
                            cursor = tmp

                        else:
                            cursor['right'] = {'value': (x, y)}
                            break
                    else:
                        if y > cursor['value'][1]:
                            tmp = cursor.get('left', {})
                            if tmp:
                                cursor = tmp
                            else:
                                cursor['left'] = {'value': (x, y)}
                                break
                        elif y < cursor['value'][1]:
                            tmp = cursor.get('right', {})
                            if tmp:
                                cursor = tmp

                            else:
                                cursor['right'] = {'value': (x, y)}
                                break
                        else:
                            break
        buff = [tree]
        count, last = 0, None
        while buff:
            while buff[-1].get('left', None):
                buff.append(buff[-1]['left'])
            while buff and not buff[-1].get('right', None):
                this = buff.pop(-1)
                if count == 0:
                    count, last = 1, this['value'][1]
                else:
                    if this['value'][1] > last:
                        count, last = count + 1, this['value'][1]

                # ret.append(buff.pop(-1))
            if buff:
                # ret.append(buff.pop(-1))
                this = buff.pop(-1)
                if count == 0:
                    count, last = 1, this['value'][1]
                else:
                    if this['value'][1] > last:
                        count, last = count + 1, this['value'][1]
                buff.append(this['right'])
        return count
