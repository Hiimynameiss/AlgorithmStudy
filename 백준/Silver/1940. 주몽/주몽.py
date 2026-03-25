import sys
input = sys.stdin.readline

ingredient_count = int(input())
complete = int(input())
ingredients = list(map(int, input().split()))
ingredients.sort()

count = 0
start_index = 0
end_index = ingredient_count - 1

while start_index < end_index:
	if ingredients[start_index] + ingredients[end_index] < complete:
		start_index += 1
	elif ingredients[start_index] + ingredients[end_index] > complete:
		end_index -= 1
	else:
		count += 1
		start_index += 1
		end_index -= 1
		
print(count)