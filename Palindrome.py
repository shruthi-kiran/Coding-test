word = input("Enter the string: ")
def check_palindrome(word):
    word1=word
    word=word.casefold()
    rev = reversed(word)
        
    if list(word) == list(rev):
      print(word1, " is a palindrome ")
    else:
      print(word1," is not a palindrome")

check_palindrome(word)