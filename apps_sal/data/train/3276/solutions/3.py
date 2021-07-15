def missing(nums, str):
    str = str.replace(' ', '').lower()
    if max(nums) >= len(str):
        return "No mission today"
    return ''.join( str[c] for c in sorted(nums) )
