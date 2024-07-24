# Tuple allows duplicate values
# Any type of data can be stored
# We cannot modify the tuple item . we cannot add or remove

a = (1,2,3,4,5)
b = list(a)
print(a) # (1, 2, 3, 4, 5)
b.pop()
print(b) # [1, 2, 3, 4]