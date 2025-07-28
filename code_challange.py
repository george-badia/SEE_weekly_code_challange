# 1. Program to create a list of integers and compute their sum
def sum_of_integers():
    numbers = []
    while True:
        user_input = input("Enter an integer (or 'done' to finish): ")
        if user_input.lower() == 'done':
            break
        try:
            number = int(user_input)
            numbers.append(number)
        except ValueError:
            print("Please enter a valid integer.")
    total = sum(numbers)
    print(f"The sum of the integers is: {total}")

