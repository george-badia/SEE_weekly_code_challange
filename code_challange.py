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

# 2. Tuple of favorite books with for loop
def print_favorite_books():
    favorite_books = ("The Great Gatsby", "1984", "To Kill a Mockingbird", "Pride and Prejudice", "The Catcher in the Rye")
    for book in favorite_books:
        print(book)

# 3. Dictionary to store person information
def store_person_info():
    person = {}
    person['name'] = input("Enter your name: ")
    try:
        person['age'] = int(input("Enter your age: "))
    except ValueError:
        print("Invalid age, setting to 0")
        person['age'] = 0
    person['favorite_color'] = input("Enter your favorite color: ")
    print("Person information:", person)
