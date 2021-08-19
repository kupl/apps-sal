class Solution:

    def maxPower(self, s: str) -> int:
        count = 0
        new_count = 0
        for (i, char) in enumerate(s):
            print(char)
            try:
                if s[i + 1] == char:
                    new_count += 1
                else:
                    print('afwww')
                    if new_count >= count:
                        count = new_count
                    new_count = 0
            except:
                print('sefesf')
                if new_count >= count:
                    print('sfwafawfawfawfawfawf')
                    count = new_count
                    new_count = 0
                break
        return count + 1
