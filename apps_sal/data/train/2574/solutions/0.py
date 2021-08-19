import re
import sys
n = int(input())
for line in sys.stdin:
    remove_and = re.sub('(?<= )(&&)(?= )', 'and', line)
    remove_or = re.sub('(?<= )(\\|\\|)(?= )', 'or', remove_and)
    print(remove_or, end='')
