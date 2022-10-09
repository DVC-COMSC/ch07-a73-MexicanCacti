

numbers = [5, 20, 30, 35, 50]

insval = int(input('Enter the insertion value: '))
# ******************************
# Make your Code
# ******************************
index = -1
for i in range(len(numbers)):
    if(insval <= numbers[i]):
        index = i
        break
if index != -1:
    numbers.insert(index,insval)
print (numbers)
