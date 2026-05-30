# What does loop in code

# It repeats steps

# for i in [0,1,2,3,4,5,6,7,8,9]
for i in range(10):
    print(i)
# first loop
# i = 0 -> print(i) = print(0)
# second loop
# i = 1 -> print(i) = print(1)
...
# tenth loop
# i = 9 -> print(i) = print(9)

# the list here [5,6,7]
for i in range(5, 8):
    print(i)

# [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
for i in range(0,101, 10):
    print(i)

for i in range(0,101):
    print(i)
    i = i + 10

for i in range(1,1001):
    if i % 2 == 0:
        print(i)
n = int(input())
n2 = int(input())
tally = 0
for i in range(n): # big for loop, loops n loops, 1 time
    for j in range(n2): # med for loop, n times, n2 loops
        for k in range(n2): # small for loop, has n2 loops, n x n2 times
            tally = tally + 1        # n x n2 x n2 times
print(tally)


tally = 0 
for i in range(n):
    for j in range(n2):
        tally = tally + 1

    for k in range(n):
        for p in range(n):
            tally = tally + 1

print(tally)
