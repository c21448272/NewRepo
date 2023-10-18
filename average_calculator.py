# Function to calculate the average of a list of numbers
def calculate_average(numbers):
    if len(numbers) == 0:
        return 0  # Avoid division by zero for an empty list
    total = sum(numbers)
    average = total / len(numbers)
    return average

# Input a list of numbers (e.g., [1, 2, 3, 4, 5])
numbers = [int(x) for x in input("Enter a list of numbers separated by spaces: ").split()]

# Calculate and print the average
average = calculate_average(numbers)
print(f"The average of the numbers is: {average}")

