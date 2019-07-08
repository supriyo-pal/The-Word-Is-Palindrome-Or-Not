def check_palindrome(word):
    rev=word[::-1]
    print("String :",word)
    print("Reversed string :",rev)
    if(rev==word):
      return True
    else:
        return False
status=check_palindrome("malayalam")
if(status):
    print("word is palindrome")
else:
    print("word is not palindrome")