def is_palindrome(text):
    new_text = text.replace(" ", "").lower()
    return new_text == new_text[::-1]

# level, Hello, racecar, A man a plan a canal Panama

print(is_palindrome('level'))
print(is_palindrome('Hello'))
print(is_palindrome('racecar'))
print(is_palindrome('A man a plan a canal Panama'))
   

