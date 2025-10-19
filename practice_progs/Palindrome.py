def isPalindrome(str) :
    for i in range(len(str)//2):
        if str[i] != str[len(str)-i-1]:
            print("Not a palindrome")
    print("Is a palindrome")
    return True

s = "racecar"
print (isPalindrome(s))