# Write a function that takes a string and returns true if 
# it's a palindrome (ignoring spaces and cases).



# def stringChecker():
#     word = input()
#     word = word.replace("","").lower()
#     i = 0
#     j = len(word)-1
#     while i < j:
#         if word[i] != word[j]:
#             return "false"
#         i += 1
#         j -= 1
#     return "true"

# print(stringChecker())    


# reversing a string 

# word = input("enter you name:")
# reverse_word = ""
# for i in range(len(word)-1,-1,-1):
#     reverse_word  = reverse_word + word[i]
# print(reverse_word)



# Checking if a string is palindrome(another way)

# string = input("Enter any word:")
# reverse_word = ""
# for i in range(len(string)-1,-1,-1):
#     reverse_word = reverse_word + string[i]
   
# if string == reverse_word:
#     print("true","",string," ",reverse_word)
# else:
#     print("not a palindrome")  



# Longest Word in a Sentence
# Given a string sentence, write a function to return the longest
# word in it. Ignore punctuation.
   
# sentence = input()
# words = sentence.split()

# longest = ""
# for word in words:
#     if len(word) > len(longest):
#         longest = word

# print(longest)



