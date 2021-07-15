t=int(input())
for i in range(t):
    n,k=list(map(int,input().split(" ")))
    arr=list(map(int,input().strip().split(" ")))[:n]
    def maxCircularSum(arr, n, k):
        if (n < k):
            print("Invalid");
            return;

        sum = 0;
        start = 0;
        end = k - 1;

        for i in range(k):
            sum += arr[i];

        ans = sum;

        for i in range(k, n + k):
            sum += arr[i % n] - arr[(i - k) % n];

            if (sum > ans):
                ans = sum;
                start = (i - k + 1) % n;
                end = i % n;

        print(ans);

    def __starting_point():
        maxCircularSum(arr, n, k);
__starting_point()
