import sys
input = sys.stdin.readline

# 1. 입력 받기
n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

# 2. 2차원 구간 합 배열(dp) 생성 및 초기화
dp = [[0] * (n + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, n + 1):
        # 1단계 공식 적용
        dp[i][j] = dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1] + arr[i-1][j-1]

# 3. 쿼리 처리
for _ in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    # 2단계 공식 적용
    result = dp[x2][y2] - dp[x1-1][y2] - dp[x2][y1-1] + dp[x1-1][y1-1]
    print(result)