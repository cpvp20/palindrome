def reverse (x):        #make a function to reverse a string
    x = (x)[::-1]
    return(x)
#ACTUAL CODE
print("hello")
print("tell me words, i'll tell you which ones are palindromes")
print("and i'll give you a cookie")
x= input("type them now please ")   #make a variable of the words
y= x.split(" ")     #make a list of the words (splitting turns a string into a list)
for word in y:
    palindrome=reverse(word)    #reverse each word
    if word==palindrome:
        print(word, "is a palindrome")
    if word!=palindrome:
        print("'",word,"'", "is not a palindrome")
print("I was kidding about the cookie, bye now")
