# print out all combinations of a 6-sided dice
# for example

# 1 1
# 1 2 
# 1 3
# 1 4
# ...
# 6 5
# 6 6

nums= int(input(" give a number for the number of sides the dice should have"))
for a in range(nums + 1):
    for b in range(nums + 1):
     print(str(a) + " " + str(b))
