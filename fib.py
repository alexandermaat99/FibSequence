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

seq = [0,1]

if totalNum > 2:
    totalNum -= 2
    a = 0
    b = 1
    
    for i in range(totalNum):
        fib = seq[a] + seq[b]
        seq.append(fib)
        a += 1
        b += 1


print(seq)