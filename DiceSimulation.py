import numpy as np 

num_rolls=1000

rolls=np.random.randint(1,7,num_rolls)

counts=np.bincount(rolls)[1:]

percentages = (counts / num_rolls) * 100

for i in range(1,7):
    print(f"numer {i} was rolled {counts[i-1]} times, which is {percentages[i-1]:.2f}% of the rolls")

max_Value_index=np.argmax(counts) + 1
min_value_index=np.argmin(counts) + 1

print(f"\nThe most rolled number is {max_Value_index} with {counts[max_Value_index-1]} rolls ({percentages[max_Value_index-1]:.2f}%)")
print(f"The least rolled number is {min_value_index} with {counts[min_value_index-1]} rolls ({percentages[min_value_index-1]:.2f}%)")
