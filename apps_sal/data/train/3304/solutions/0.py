def is_inertial(arr):
    mx   = max(arr, default=1)
    miO  = min((x for x in arr if x%2==1), default=float("-inf"))
    miE2 = max((x for x in arr if x%2==0 and x!=mx), default=float("-inf"))
    return mx%2 == 0 and miE2 < miO
