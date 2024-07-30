dict1 = {'a': [1, 2], 'b': [3, 4]}
dict2 = {'c': [1, 5], 'd': [2, 6]}

for key1, value1 in dict1.items():
    for key2, value2 in dict2.items():
        if value2[0] in value1:
            dict2[key2][0] = value1[0]

print(dict2)
# Output: {'c': [1, 5], 'd': [1, 6]}
