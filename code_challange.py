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

# 4. Program to find common elements in two sets
def common_elements():
    set1 = set()
    set2 = set()
    
    print("Enter integers for first set (enter 'done' to finish):")
    while True:
        user_input = input("Enter an integer: ")
        if user_input.lower() == 'done':
            break
        try:
            set1.add(int(user_input))
        except ValueError:
            print("Please enter a valid integer.")
    
    print("Enter integers for second set (enter 'done' to finish):")
    while True:
        user_input = input("Enter an integer: ")
        if user_input.lower() == 'done':
            break
        try:
            set2.add(int(user_input))
        except ValueError:
            print("Please enter a valid integer.")
    
    common = set1.intersection(set2)
    print(f"Common elements: {common}")

# 5. List comprehension for words with odd length
def odd_length_words():
    words = ["apple", "banana", "cat", "dog", "elephant", "fish", "grape"]
    odd_length = [word for word in words if len(word) % 2 != 0]
    print("Words with odd number of characters:", odd_length)

# Run all programs
if __name__ == "__main__":
    print("1. Sum of Integers")
    sum_of_integers()
    
    print("\n2. Favorite Books")
    print_favorite_books()
    
    print("\n3. Person Information")
    store_person_info()
    
    print("\n4. Common Elements in Sets")
    common_elements()
    
    print("\n5. Words with Odd Length")
    odd_length_words()