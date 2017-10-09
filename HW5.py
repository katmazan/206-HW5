##Katarina Mazanka
import re
filename = 'regex_sum_38687.txt'
file_object = open(filename, "r")
text = file_object.read()
numbers = re.findall(r'[0-9]+', text)
num_sum = 0
for item in numbers:
    item = int(item)
    num_sum += item
print(num_sum)

