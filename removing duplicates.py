numbers=[1,2,4,2,6,8,7,3,4,5,6,7,8,9,0]
num=[]
for number in numbers:
    if number not in num:
        num.append(number)
        num.reverse()
print(num)        
