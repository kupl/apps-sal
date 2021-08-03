def missing(nums, str):
    return ''.join([str.replace(" ", "").lower()[i] for i in sorted(nums)]) if max(nums) < len(str.replace(" ", "")) else "No mission today"
