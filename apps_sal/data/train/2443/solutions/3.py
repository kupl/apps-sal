class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        text = list(text)
        text2 = ['a', 'b', 'l', 'n', 'o']
        num1 = [1, 1, 2, 1, 2]
        nums2 = []
        for j in range(len(text2)):
            k = len([number for number in text if number == text2[j]])
            #print([number for number in text if number ==text2[j]])
            nums2.append(k)
        print(nums2)
        rt = []
        for j in range(len(nums2)):
            rt.append(nums2[j] / num1[j])

        return int(min(rt))
