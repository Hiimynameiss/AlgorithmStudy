n = int(input()) # n을 숫자로 미리 변환
# input().split()을 써야 공백을 기준으로 숫자를 잘라옵니다.
scores = list(map(int, input().split())) 

total_sum = 0
max_val = 0

for i in scores:
    total_sum += i # 이미 위에서 int로 바꿨으므로 i만 더하면 됨
    if max_val < i:
        max_val = i

# n은 위에서 int로 변환했으므로 그대로 사용
result = total_sum * 100 / max_val / n
print(result)