largest_arrangement=lambda a:(lambda l:int(''.join(sorted(map(str,a),key=lambda s:s.ljust(l,s[0]))[::-1])))(len(str(max(a))))
