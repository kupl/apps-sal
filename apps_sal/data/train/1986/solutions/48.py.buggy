class Solution:
\tdef circularPermutation(self, n: int, start: int) -> List[int]:
\t\tres=[]
\t\tfor i in range(2**n):
\t\t\tres.append(i^(i>>1))
\t\tstack=[]
\t\ttem=[]
\t\tfor j in range(len(res)):
\t\t\tif res[j]!=start:
\t\t\t\tstack.append(res[j])
\t\t\telse:
\t\t\t\ttem=res[j:]
\t\t\t\tbreak
\t\tans=tem+stack
\t\treturn ans

