sum = 0
for i in range(3, 1000):
    if i % 5 == 0 or i % 3 == 0:
        sum += i
print("The sum of all the multiples of 3 or 5 below 1000 is " + str(sum))
input()

#233168