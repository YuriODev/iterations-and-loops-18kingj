# Your solution to Exercise 14
num_of_int = int(input())
sum = 0
for i in range(num_of_int):
    num = int(input())
    if num == 0:
        sum += 1
print(sum)