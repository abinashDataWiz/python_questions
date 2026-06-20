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
# [0,1,2,3,4,5,6,7,8,9....,100]
for i in range(0,101):
    print(i)
    i = i + 10

for i in range(1,1001):
    if i % 2 == 0: # if i is even
        print(i)
n = int(input())
p = int(input())
tally = 0
for i in range(n): # big for loop, loops n loops, 1 time
    for j in range(p): # med for loop, n times, p loops
        for k in range(p): # small for loop, has p loops, n x p times
            tally = tally + 1        # n x p x p times
print(tally)



tally = 0
for i in range(n):
    tally+=1
for j in range(p):
    tally+=1

print(tally) # n + n2


n = int(input())
p = int(input())
p = int(input())
tally = 0 
for i in range(n):
    for j in range(p):
    for j in range(p):
        tally = tally + 1

    for k in range(n):
        tally = tally + 1

print(tally) # n x p + n x n = n x (p + n)
print(tally) # n x p + n x n = n x (p + n)

# What if tally = n x (p + n x n)

for i in range(n):
    for i in range(p):
        tally = tally + 1 
for i in range(n):
    for i in range(p):
        tally = tally + 1 

    for i in range(n):
        for i in range(n):
            tally = tally + 1b
    for i in range(n):
        for i in range(n):
            tally = tally + 1b

print(tally)
print(tally)




# Divide and conquer
# n*(n^6 + n2) + n^2 *(n2 + n^3)
