from hashlib import sha256
from itertools import permutations as p
sha256_cracker=lambda h,c:next((''.join(i) for i in p(c) if sha256(''.join(i).encode()).hexdigest()==h),None)
