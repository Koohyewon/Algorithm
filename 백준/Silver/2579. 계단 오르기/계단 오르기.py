import sys

n = int(sys.stdin.readline())

stairs = [0] * (n + 1)
for i in range(1, n + 1):    
    stairs[i] = int(sys.stdin.readline())

dp = [0] * (n + 1)
dp[1] = stairs[1]

if n > 1:
    dp[2] = stairs[1] + stairs[2]

for i in range(3, n + 1):
    dp[i] = max(stairs[i] + dp[i - 2], stairs[i] + stairs[i - 1] + dp[i - 3])

print(dp[n])