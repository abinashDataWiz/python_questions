# What is a while loop

# As long as whatever condition you have is true, 
# it will repeat your command until your condition is false


# Syntax for while loop

while(boolean expression):
    # body of code inside while loop


i = 0 

while i < 100:
    print(i)
    i+=1


i = 0 

while i != 100:
    for j in range(i):
        print("hello") # how many times is this line running? 
    i+=1
