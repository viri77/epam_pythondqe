import random

#generate list of random numbers
b = [random.randint(0,1000) for i in range(100)]



# create empty lists for even and odd numbers
list_even = []
list_odd=[]

#variables for calculating avg
avg_even = 0
avg_odd = 0

#cycle for defining odd and even numbers
for i in b:
    if i % 2 == 0:
        list_even.append(i)

    else:
        list_odd.append(i)

#calculating average for even and odd
avg_even = sum(list_even) / len(list_even)
avg_odd = sum(list_odd)/len(list_odd)


print(avg_even)
print(avg_odd)





