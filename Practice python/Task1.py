nums = input().split()

result = []

for x in nums:
    number = int(x)
    if number % 2 == 0:
        result.append(number * 2)

for x in result:
    print(x, end=" ")