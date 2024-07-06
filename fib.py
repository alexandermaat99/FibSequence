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