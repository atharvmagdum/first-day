# A)
text = input("Enter the Text :")
print("Input text is :",text)
num = len(text)
print("Number of characters :",num)
#Output--> Number of characters : ??

# B)
words = text.split()
num = len(words)
print("Total Words are :",num)
#Output--> Total Words are : ??

# C)
count = 0
for c in text:
    if c == 'a' or c == 'A' or c == 'e' or c == 'E' or c == 'i' or c == 'I' or c == 'o' or c == 'O' or c == 'u' or c == 'U':
        count = count+1
print("Number of vowels present :", count)
