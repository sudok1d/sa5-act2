def check_palindrome(text):
    if text == text[::-1]:
        print(f"{text} is a palindrome")
    else:
        print(f"{text} is not a palindrome")


<<<<<<< HEAD
<<<<<<< HEAD
text = "did"
# text = "hello"
=======
text = input("Enter text to check for palindrome: ")
>>>>>>> 2e4bb72 (Replaced hardcoded string with user-input text string)
check_palindrome(text)
=======
try:
    filepath = input("Enter filepath for palindrome check: ")
    text = open(filepath, "r").read()
    check_palindrome(text)
except OSError:
    print(f"Unable to process file at {filepath}")
>>>>>>> 6148c90 (Replaced hardcoded text string with filepath input and read file content)
