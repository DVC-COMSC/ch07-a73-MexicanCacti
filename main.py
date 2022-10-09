

numbers = [5, 20, 30, 35, 50]

insval = int(input('Enter the insertion value: '))
# ******************************
# Make your Code
# ******************************
for i in range(len(numbers)):
    if(insval <= numbers[i]):
        index = i
        break
numbers.insert(index,insval)

print(index)
print (numbers)
