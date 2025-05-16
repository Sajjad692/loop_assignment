# Using a for Loop
# for loop is used when the number of repitation known in advance.

for numbers in range(1,11):
    print(numbers)

# Using a while Loop
# while loop is used when numbers of repitation is not known,
# but loop should continue as long as condition is true.

number=1
while number<=5:
    print(number)
    number+=1

# Loop with a Condition
# Ask the user for a number and use a while loop to count down to 1.

num=int(input("Enter the number: "))
while num>=1:
    print(num)
    num-=1

# what we can do if user entered 0 or -3???

while True:
    try: # handle non integer inputs
        num=int(input("Please Enter a positive number: "))
        if num<1: # if statement warn the user for 0 input
            print("Please enter a number greater than 0.")
        else:
            break
        
    except ValueError: # handle non integer inputs
        print("Invalid number, please enter a valid number")

# Countdown starts here
while num >= 1:
    print(num)
    num -= 1

# Nested Loops
# when there is another loop inside the loop this type of loop is called nested loop.
# Print a mini multiplication table for numbers 1 to 3 

for i in range(1,4):
    for j in range(1,4):
        result=i*j
        print(f"{i:<2}X {j:<2}={result:>2}")

# Using break 

for i in range(11):
    if i == 6:
        break
    print(i)

# Using continue

for i in range(6):
    if i == 3:
        continue
    print(i)