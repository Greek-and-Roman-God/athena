# 병사 배치하기

n=int(input())
ns=list(map(int, input().split()))
ns.reverse()

dp=[1]*n
for i in range(1,n):
    for j in range(0, i):
        if ns[i]>ns[j]:
            dp[i]=max(dp[i], dp[j]+1)

print(n-max(dp))