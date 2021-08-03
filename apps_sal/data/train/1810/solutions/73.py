class Information:
    def __init__(self):
        self.next = 0
        self.used = set()


class Solution:
    def getFolderNames(self, names: List[str]) -> List[str]:
        result, occupied = [], collections.defaultdict(Information)

        for name in names:
            if name in occupied:
                info = occupied[name]
                while info.next in info.used:
                    info.used.remove(info.next)
                    info.next += 1
                final_name = name if info.next == 0 else '{}({})'.format(name, info.next)
            else:
                final_name = name

            if final_name[-1] == ')':
                scan = len(final_name) - 2
                while scan >= 0 and final_name[scan].isdigit():
                    scan -= 1

                if scan >= 0 and final_name[scan] == '(' and int(final_name[scan + 1: -1]) > 0:
                    occupied[final_name[:scan]].used.add(int(final_name[scan + 1: -1]))

            occupied[name].next += 1
            if name != final_name:
                occupied[final_name].next += 1

            result.append(final_name)
        return result
