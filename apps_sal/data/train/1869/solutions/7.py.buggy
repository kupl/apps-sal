from typing import Tuple

class TreeNode:
\tdef __init__(self, val, left=None, right=None):
\t\tself.val = val
\t\tself.left = left
\t\tself.right = right

class Solution:

\tdef _tokenize(self, s) -> Tuple[str, int]:
\t\tout = []
\t\tcur = \"num\"

\t\tfor c in s:

\t\t\tif c == \"-\":
\t\t\t\tnew = \"dash\"
\t\t\telse:
\t\t\t\tnew = \"num\"

\t\t\tif cur == new:
\t\t\t\tout.append(c)
\t\t\telse:
\t\t\t\tyield cur, \"\".join(out)
\t\t\t\tout = [c]
\t\t\t\tcur = new

\t\tyield cur, \"\".join(out)

\tdef tokenize(self, s):
\t\tfor type, token in self._tokenize(s):
\t\t\tif type == \"num\":
\t\t\t\tyield type, int(token)
\t\t\telse:
\t\t\t\tyield type, len(token)

\tdef recoverFromPreorder(self, S: str) -> TreeNode:

\t\tit = self.tokenize(S)
\t\t_, val = next(it)

\t\tm = {0: TreeNode(val)}
\t\tlevel = 0

\t\tfor type, value in it:
\t\t\tif type == \"dash\":
\t\t\t\tlevel = value
\t\t\t\tcontinue

\t\t\tn = TreeNode(value)
\t\t\tm[level] = n

\t\t\tif m[level - 1].left is None:
\t\t\t\tm[level - 1].left = n
\t\t\telse:
\t\t\t\tm[level - 1].right = n

\t\treturn m[0]

