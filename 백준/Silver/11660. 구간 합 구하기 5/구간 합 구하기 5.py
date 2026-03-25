import sys
input = sys.stdin.readline

# n(배열의 크기), m(합을 구해야 하는 횟수)
n, m = map(int, input().split())
# 본래 리스트
table = [list(map(int, input().split())) for _ in range(n)]
# 구간 합 배열 생성
dp = [[0] * (n+1) for _ in range(n + 1)]

# 구간 합 배열 초기화
for i in range(1, n+1):
	for j in range(1, n+1):
		dp[i][j] = dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1] + table[i-1][j-1]
		
# 쿼리 처리
for _ in range(m):
	x1, y1, x2, y2 = map(int, input().split())
	result = dp[x2][y2] - dp[x1-1][y2] - dp[x2][y1-1] + dp[x1-1][y1-1]
	print(result)