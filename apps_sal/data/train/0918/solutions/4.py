'''
using namespace std; 

main(){
    long long a=pow(2,1000000000000000000,8589934592);
    printf("%lld",a);
}'''
a = int(input())
for i in range(a):
    b = int(input())
    aa = pow(2, b, 8589934592)
    print("Case", str(i + 1) + ":", (aa - 1) % (8589934592))
