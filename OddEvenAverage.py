even = []
odd = []

numfile = open("mynumbers.txt", "r")

for line in numfile:

    #printing line to check if the reading is correct
    print(line)
    # checking each number in a line and adding it to the corresponding apt list
    for char in line.split():
        
           if (int(char))%2 == 0:
              even.append(int(char))
           
           else:
              odd.append(int(char))

numfile.close()
# getting the sum and rounding it
even_avg = round(sum(even)/len(even),4)
odd_avg = round(sum(odd)/len(odd),4)

print('\n' + 'Average of the even numbers: '+str(even_avg))
print('Average of the odd numbers: '+str(odd_avg))
