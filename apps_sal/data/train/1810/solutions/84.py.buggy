class Solution:
    \"\"\"
    字典 key：string value：值为该字符串下一个可能的最小正整数。
    如果遇到一个字符串，不在哈希表中，则将其本身放入返回结果数组，然后在哈希表中创建键为该字符串值为 1 的新项。
    如果遇到的字符串在哈希表中，则在该字符串后尝试加入后缀，后缀的值从哈希表中的值开始，每次加 1 找到最小没有被占用的后缀值（即拼接后没有出现在哈希表中），然后将拼接好的字符串放入哈希表中，值为 1。且更新原来字符串的value
    O(N*L)
    \"\"\"
    def getFolderNames(self, names: List[str]) -> List[str]:
        res = []
        records = {}
        for name in names:
            if name not in records:
                records[name] = 1
                res.append(name)
            else:
                start = records[name]
                while name+\"(\"+str(start)+\")\" in records:
                    start += 1
                res.append(name+\"(\"+str(start)+\")\")
                records[name] = start
                records[name+\"(\"+str(start)+\")\"] = 1
        return res
                
            
        
