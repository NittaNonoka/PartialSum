n  = int(input())
a_list = list(map(int, input().split()))
A = int(input())

# dp[i+1][j] : i番目までの整数で総和がjになるようにすることが可能か(True or False)
# i = 0,..,n  j = 0,..,A
# dp[0][j](j=0,..,A) : 何も選ばない
# dp[1][j](j=0,..,A) : 一番目までの整数で総和がjになるようにすることが可能か
# ...
# 漸化式を作る
# 選ぶ場合
# dp[i+1][j] = dp[i][j-a]
# 選ばない場合
# dp[i+1][j] = dp[i][j]
# どちらかがTrueならTrue

# 初期値　False (dp[0][0]のみTrue)

dp = [[False for _ in range(A+1)] for _ in range(n+1)]
dp[0][0] = True


for i, a in enumerate(a_list):
    for j in range(A+1):
        select = False
        noSelect = False
        if j < a:
            dp[i+1][j] |= dp[i][j]
        else:
            select |= dp[i][j-a]
            noSelect |= dp[i][j] 
            dp[i+1][j] = select or noSelect

if dp[n][A]:
    print("Yes")
else:
    print("No")