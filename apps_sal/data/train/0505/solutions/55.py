class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        mystack_bracket, mystack_letter = [], []
        pos = 0
        for i in s:
            if i == '(':
                mystack_bracket.append((i, pos))
                # print(\"1\", mystack_bracket)
            elif i == ')':
                if len(mystack_bracket) != 0:
                    y = mystack_bracket.pop()
                    mystack_letter.append(y)
                    mystack_letter.append((i, pos))
                    # print(\"2:\",mystack_letter)
            else:
                mystack_letter.append((i, pos))
                # print(\"3:\",mystack_letter)

            pos += 1

        return ''.join(i for i, j in sorted(mystack_letter, key=lambda mystack_letter: mystack_letter[1]))
