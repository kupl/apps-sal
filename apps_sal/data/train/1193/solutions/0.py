MAX = 100005
tree = [0] * MAX; 
lazy = [0] * MAX;
 
def updateRangeUtil(si, ss, se, us, ue, diff) :
    if (lazy[si] != 0) :
        tree[si] += lazy[si];
        if (ss != se) :
            lazy[si * 2 + 1] += lazy[si];
            lazy[si * 2 + 2] += lazy[si];
        lazy[si] = 0;
 
    if (ss > se or ss > ue or se < us) :
        return; 
 
    if (ss >= us and se <= ue) :
        tree[si] += diff;
        if (ss != se) :
            lazy[si * 2 + 1] += diff;
            lazy[si * 2 + 2] += diff;
        return; 
 
    mid = (ss + se) // 2;
    updateRangeUtil(si * 2 + 1, ss,mid, us, ue, diff);
    updateRangeUtil(si * 2 + 2, mid + 1,se, us, ue, diff);
    tree[si] = min(tree[si * 2 + 1],tree[si * 2 + 2]); 
 
def updateRange(n, us, ue, diff) : 
    updateRangeUtil(0, 0, n - 1, us, ue, diff); 
 
def getSumUtil(ss, se, qs, qe, si) :
    if (lazy[si] != 0) :
        tree[si] += lazy[si];
        if (ss != se) :
            lazy[si * 2 + 1] += lazy[si];
            lazy[si * 2 + 2] += lazy[si];
        lazy[si] = 0;
 
    if (ss > se or ss > qe or se < qs) :
        return 10e9; 
 
    if (ss >= qs and se <= qe) :
        return tree[si]; 
 
    mid = (ss + se) // 2; 
    return min(getSumUtil(ss, mid, qs, qe, 2 * si + 1),getSumUtil(mid + 1, se, qs, qe, 2 * si + 2)); 
 
def getSum(n, qs, qe) : 
    if (qs < 0 or qe > n - 1 or qs > qe) :
        #print("Invalid Input", end = "");
        return -1;
 
    return getSumUtil(0, n - 1, qs, qe, 0); 
 
def constructSTUtil(arr, ss, se, si) : 
    if (ss > se) :
        return;
    if (ss == se) :
        tree[si] = arr[ss];
        return; 
    mid = (ss + se) // 2;
    constructSTUtil(arr, ss, mid, si * 2 + 1);
    constructSTUtil(arr, mid + 1, se, si * 2 + 2);
    tree[si] = min(tree[si * 2 + 1], tree[si * 2 + 2]); 
 
def constructST(arr, n) :
    constructSTUtil(arr, 0, n - 1, 0); 
 
# Driver code 
for _ in range(int(input())):
    tree = [0] * MAX; 
    lazy = [0] * MAX;
    n=int(input());
    y=int(input());
    arr=[1]*n;
    constructST(arr, n);
    for xyz in range(y):
        l,r=list(map(int,input().split()));
        updateRange(n, l, r, getSum(n, l, r)%1000000007);
    print((getSum(n, 0, n-1)%1000000007));

