def check_palindrome(text):
    if text == text[::-1]:
        print(f"{text} is a palindrome")
    else:
        print(f"{text} is not a palindrome")


<<<<<<< HEAD
text = "did"
# text = "hello"
=======
text = input("Enter text to check for palindrome: ")
>>>>>>> 2e4bb72 (Replaced hardcoded string with user-input text string)
check_palindrome(text)
