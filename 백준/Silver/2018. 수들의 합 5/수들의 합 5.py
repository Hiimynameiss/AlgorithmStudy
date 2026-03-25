import sys

n = int(sys.stdin.readline())

count = 1  # 자기 자신(n)을 미리 카운트
start_index = 1
end_index = 1
current_sum = 1

while end_index != n:
    if current_sum == n:
        count += 1
        end_index += 1
        current_sum += end_index
    elif current_sum < n:
        end_index += 1
        current_sum += end_index
    else:                         
		    # current_sum > n
        current_sum -= start_index
        start_index += 1

print(count)