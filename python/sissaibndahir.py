sum = 0

for i in range(64):
    ricegrain =  2**i
    sum = sum + ricegrain
    print("Iteration {}: Rice per field = {:>30,}, Total = {:>30,}".format(i, ricegrain, sum))

weightintons = sum * 0.02 / 1000 / 1000
print("Weight: {:,.0f} metric tons".format(weightintons))
