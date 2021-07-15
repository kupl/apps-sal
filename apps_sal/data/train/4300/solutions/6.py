def solve_dp (needle, haystack):
    # let prefixes[h][n] = number of n-letters-long prefixes
    #                      ending in h-th position of haystack
    N, H = len(needle), len(haystack)
    prefixes = [[1] + N*[0] for h in range(H)]
    
    def match (h, n): return haystack[h] == needle[n-1]
    prefixes[0][1] = 1 if match(0, 1) else 0

    for h in range(1, H):
        max_prefix_len = min(h+1, N)
        for n in range(1, max_prefix_len+1):
            with_current = prefixes[h-1][n-1] if match(h, n) else 0
            without_current = prefixes[h-1][n]
            prefixes[h][n] = with_current + without_current
    return prefixes[H-1][N]

def solve_recursive (needle, haystack):
    if not needle or needle == haystack: return 1
    if not haystack: return 0
    
    needle_head, *needle_tail = needle
    haystack_head, *haystack_tail = haystack
    match = needle_head == haystack_head
    
    head_matches = solve_recursive(needle_tail, haystack_tail) if match else 0
    tail_matches = solve_recursive(needle, haystack_tail)
    return head_matches + tail_matches

def solve (needle, haystack, method=solve_dp):
    return method(needle, haystack)


