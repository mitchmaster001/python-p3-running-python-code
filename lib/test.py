numbers = [10, 4, 7, 32, 3, 8]

# Find the largest number
largest = numbers[0]
for num in numbers:
    if num > largest:
        largest = num

# Find the smallest number
smallest = numbers[0]
for num in numbers:
    if num < smallest:
        smallest = num

# Find the second-largest number
second_largest = float('-inf')
for num in numbers:
    if num > second_largest and num < largest:
        second_largest = num

print(f"The largest number is {largest}")
print(f"The smallest number is {smallest}")
print(f"The second-largest number is {second_largest}")