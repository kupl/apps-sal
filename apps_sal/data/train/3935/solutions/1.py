def vowel_recognition(input):
    chars = input.lower()
    N = len(chars)
    count = 0
    
    for i, c in enumerate(chars):
        if c in 'aeiou':
            count += (N - i) * (i + 1)
            
    return count
