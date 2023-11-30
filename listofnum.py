print("Enter a list of numbers, type 0 when finished.")

numbers = []
number = -1

while number != 0:
    number = int(input("Enter number: "))

    if number != 0:
        numbers.append(number)

sum = 0

for number in numbers:
    sum += number

print(f"The sum is: {sum}")
count = len(numbers)
average = sum / count

print(f"The average is: {average}")

best_so_far = -1

for number in numbers:
    if number > best_so_far:
        best_so_far = number


print(f"The largest number is: {best_so_far}")

smallest = 99999999999

for number in numbers:
    if number > 0 and number < smallest:
        smallest = number

print(f"The smallest positive number is: {smallest}")
sorted_list = sorted(numbers)

print("The sorted list is:")
for number in sorted_list:
    print(number)