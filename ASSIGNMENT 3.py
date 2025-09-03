#Ashley
#R246254H

#QUESTION 1

def classify_number(num):
    if num > 0:
        return "Positive"
    elif num < 0:
        return "Negative"
    else:
        return "Zero"

# Loop to get valid integer input from user
while True:
    user_input = input("Enter an integer: ")
    try:
        number = int(user_input)
        result = classify_number(number)
        print(f"The number is {result}.")
        break  # Exit the loop after successful input
    except ValueError:
        print("That's not a valid integer. Please try again.")

#QUESTION 2

def calculate_average(*args):
    """
    Calculates the average of a variable number of numeric arguments.

    Parameters:
        *args (float or int): A variable number of numeric values.

    Returns:
        float: The average of the input numbers.
               Returns 0.0 if no arguments are provided.

    Example:
        >>> calculate_average(10, 20, 30)
        20.0
    """
    if not args:
        return 0.0
    return sum(args) / len(args)

#QUESTION 3
def get_valid_number():
    while True:
        user_input = input("Please enter a number: ")
        try:
            number = float(user_input)  # You can use int(user_input) if you want only integers
            print(f"Great! You entered the number: {number}")
            return number
        except ValueError:
            print("Oops! That wasn't a valid number. Please try again.")

# Run the function
get_valid_number()

#QUESTION 4
# List of names to write to the file
names = ["Alice", "Bob", "Charlie", "Diana", "Ethan"]

# Write names to 'names.txt', each on a new line
with open("names.txt", "w") as file:
    for name in names:
        file.write(name + "\n")

# Read and print each name from the file
with open("names.txt", "r") as file:
    for line in file:
        print(line.strip())  # .strip() removes the newline character


#QUESTION 5
# Sample list of temperatures in Celsius
celsius_temps = [0, 10, 20, 30, 37, 100]

# Lambda function to convert Celsius to Fahrenheit
fahrenheit_temps = list(map(lambda c: c * 9/5 + 32, celsius_temps))

# Print the converted list
print("Celsius temperatures:", celsius_temps)
print("Fahrenheit temperatures:", fahrenheit_temps)


#QUESTION 6
def divide_numbers(numerator, denominator):
    try:
        result = numerator / denominator
        return result
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
    except TypeError:
        print("Error: Both numerator and denominator must be numbers.")


#QUESTION 7
# Custom exception class
class NegativeNumberError(Exception):
    def __init__(self, value):
        super().__init__(f"Negative number encountered: {value}")
        self.value = value

# Function that checks if a number is positive
def check_positive(number):
    if number < 0:
        raise NegativeNumberError(number)
    print(f"{number} is a positive number.")

# Demonstration using try-except
try:
    num = -10  # You can change this to test other values
    check_positive(num)
except NegativeNumberError as e:
    print(f"Exception caught: {e}")


#QUESTION 8
import random

def generate_random_numbers(count, start, end):
    """Generates a list of random integers."""
    return [random.randint(start, end) for _ in range(count)]

def calculate_average(numbers):
    """Calculates the average of a list of numbers."""
    return sum(numbers) / len(numbers)

def main():
    random_numbers = generate_random_numbers(10, 1, 100)
    average = calculate_average(random_numbers)

    print("Generated Numbers:", random_numbers)
    print("Average:", round(average, 2))

if __name__ == "__main__":
    main()


#QUESTION 9
import re

# I. Extract all email addresses from a given text
def extract_emails(text):
    email_pattern = r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+'
    return re.findall(email_pattern, text)

# II. Validate a date in the format "YYYY-MM-DD"
def is_valid_date(date_str):
    date_pattern = r'^(?:(?:19|20)\d\d)-(?:0[1-9]|1[0-2])-(?:0[1-9]|[12]\d|3[01])$'
    return bool(re.match(date_pattern, date_str))

# III. Replace all occurrences of a word with another word in a string
def replace_word(text, old_word, new_word):
    word_pattern = rf'\b{re.escape(old_word)}\b'
    return re.sub(word_pattern, new_word, text)

# IV. Split a string by all non-alphanumeric characters
def split_by_non_alphanumeric(text):
    split_pattern = r'[^a-zA-Z0-9]+'
    return re.split(split_pattern, text)

# Example usage
if __name__ == "__main__":
    sample_text = "Contact us at support@example.com or sales@company.co.uk. Visit on 2025-09-03!"
    print("Extracted Emails:", extract_emails(sample_text))
    print("Is '2025-09-03' a valid date?", is_valid_date("2025-09-03"))
    print("Replaced Text:", replace_word("The quick brown fox jumps over the lazy dog", "fox", "cat"))
    print("Split Text:", split_by_non_alphanumeric("Hello, world! This_is a test...123"))


#QUESTION 10
import socket

HOST = '127.0.0.1'  # Localhost
PORT = 65432        # Non-privileged port

try:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((HOST, PORT))
        server_socket.listen()
        print(f"Server listening on {HOST}:{PORT}...")

        conn, addr = server_socket.accept()
        with conn:
            print(f"Connected by {addr}")
            message = "Hello from server!"
            conn.sendall(message.encode('utf-8'))

except socket.error as e:
    print(f"Socket error: {e}")
except Exception as e:
    print(f"Unexpected error: {e}")


#QUESTION 11
#API stands for Application Programming Interface. It's a set of rules and protocols that allows different software applications to communicate with each other.

#For instance, you (the client) tell the waiter (API) what you want, and the waiter brings it from the kitchen (server).

#APIs are commonly used to retrieve or send data to web services, like weather info, stock prices, or social media posts.


import requests

# Define the API endpoint
url = "https://api.example.com/data"

# Send a GET request
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    data = response.json()  # Parse JSON response
    print(data)
else:
    print(f"Error: {response.status_code}")

