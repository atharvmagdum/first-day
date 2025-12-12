num = list(map(int, input("Enter the numbers (Comma Seperated) :").split(',')))
print(num)

count_even = 0
count_odd = 0

for i in num :
    if i%2 == 0:
        count_even +=1
    else:
        count_odd +=1

print("Total Even Numbers :",count_even)
print("Total Odd Numbers :",count_odd)