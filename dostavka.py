"""id132826561."""
weight_robots = sorted(list(map(int, input().split())))
limit = int(input())
i = 0  # первый элемент в списке
j = len(weight_robots) - 1  # последний элемент в списке
count = 0  # количество платформ
while i <= j:
    total_weight = weight_robots[i] + weight_robots[j]
    if total_weight <= limit:
        count += 1
        i += 1
        j -= 1
    else:
        count += 1
        j -= 1
print(count)
