def is_palindrome(s):
    return s == s[::-1]
word = "madam"
print("Palindrome" if is_palindrome(word) else "Not Palindrom")