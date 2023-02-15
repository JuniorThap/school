input("Enter your name: ")
start = float(input("Enter the current balance (THB): "))
num = int(input("Enter number of year: "))

curr = start
for i in range(num):
    curr *= 103/100
    print(f"> Balance of year no. {i+1}: {curr} THB")