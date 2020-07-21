import time
from collections import Counter
from BSTnode import BSTNode
import itertools

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure

# I believe the RUNTIME is 0(n^c)

# Replace the nested for loops below with your improvements
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)
# double_names = (Counter(names_1) - Counter(names_2)).elements()

# double_names = set(names_1).intersection(set(names_2))
# for n in double_names:
#     duplicates.append(n)

combined_names = names_1 + names_2

names_list1 = BSTNode(names_1)

# names_list1.insert(names_1)

if names_list1.contains(names_2):
    duplicates.append(names_1)

print(names_list1)
        
end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.
