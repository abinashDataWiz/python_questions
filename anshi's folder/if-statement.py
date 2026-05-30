n = int(input("n: "))
n2 = int(input("n2: "))

tally = 0


for i in range(n):
    for j in range(n2):
        tally = tally + 1 
        if tally % 2 == 1:
         print(tally)

# How do I only print out the odd numbers?