# validation
while True:
    try:
        totalNum = int(input("Enter the number of digits you want to generate (must be 2 or greater): "))
        if totalNum < 2:
            print("Please enter a number greater than 1")
        else:
            break
    except ValueError:
        print("Please enter a valid number")

# initialize the sequence
seq = [0,1]


if totalNum > 2:
    
    #account for the first two numbers
    totalNum -= 2
    a = 0
    b = 1
    
    # generate the sequence
    for i in range(totalNum):
        fib = seq[a] + seq[b]
        
        # append the new number to the sequence
        seq.append(fib)
        
        # increment the pointers
        a += 1
        b += 1


print(seq)

#closest number filter 
#numbers before or after the target number

while True:
    try:
        targetNum = int(input("Enter the target number: "))
        break
    except ValueError:
        print("Please enter a valid number")
        
closestNum = 0
closestNumIndex = 0
closestNumDiff = 0

for i in range(len(seq)):
    diff = abs(targetNum - seq[i])
    if i == 0:
        closestNum = seq[i]
        closestNumIndex = i
        closestNumDiff = diff
    elif diff < closestNumDiff:
        closestNum = seq[i]
        closestNumIndex = i
        closestNumDiff = diff
        
print(f"Closest number to {targetNum} is {closestNum} at index {closestNumIndex}")

#numbers before the target number
beforeNum = []
for i in range(closestNumIndex):
    beforeNum.append(seq[i])
    
print(f"Numbers before {targetNum}: {beforeNum}")

#numbers after the target number
afterNum = []
for i in range(closestNumIndex+1, len(seq)):
    afterNum.append(seq[i])
    
print(f"Numbers after {targetNum}: {afterNum}")
# ```

# ## Output
# ```
# Enter the number of digits you want to generate (must be 2 or greater): 10
# [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
