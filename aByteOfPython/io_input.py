def reverse(text):
    return text[::-1]

biaodian=(',',' ','.')
def is_palindrome(text):
    afterText=""
    for chr in text:
        if chr not in biaodian:
            afterText+=chr
    afterText=afterText.lower()
    print(afterText)
    return afterText == reverse(afterText)


something = input("Enter text: ")
if is_palindrome(something):
    print("Yes, it is a palindrome")
else:
    print("No, it is not a palindrome")