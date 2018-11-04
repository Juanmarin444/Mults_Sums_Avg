# Multiples
# Part 1 - write code that prints odd nums from 1 - 1000 use a for loop 
# and no list
### for x in range(1, 1000):
    ### if x % 2 == 0:
        ### continue
    ### else:
        ### print x

# Part 2 - create another program that prints all the mults of 5 from 
# 5 - 1,000,000
### for num in range(5, 1000005):
    ### if num % 5 == 0:
        ### print num
# Sum List
# Create a program that prints the sum of all the values in the list
# a = [1, 2, 5, 10, 255, 3]

a = [1, 2, 5, 10, 255, 3]
total = 0

for num in a:
     total += num
print total

# Average List
# Create a program that prints the avg of the vals in the list:
avg = total / len(a)
print avg