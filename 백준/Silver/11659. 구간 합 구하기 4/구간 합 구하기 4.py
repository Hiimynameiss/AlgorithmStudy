import sys

input = sys.stdin.readline

numbercount, sumcount = map(int, input().split())
numbers = list(map(int, input().split()))

range_sum = [0]
current_total = 0

for i in numbers:
    current_total += i
    range_sum.append(current_total)

for _ in range(sumcount):
    start, end = map(int, input().split())
    print(range_sum[end] - range_sum[start-1])