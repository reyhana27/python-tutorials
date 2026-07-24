# Arrays can hold more than one values.
# Arrays contain a list of items in them.

fruits = ['peach', 'banana', 'apple']  # this is an array called fruits and contains a list of 3 items which are fruit names

# you can refer to any element in an array by using the index number.
# the index number always starts from 0

print(fruits[0])  # this will print the first element 'peach' in the array.
print(fruits[1])  # this will print the second element 'banana' in the array.

# instead of searching for what the last element in an array is, it is smarter to write '-1' as the index number

print(fruits[-1]) # this will print out the last element in the array
# task: crate an array called city with 3 elements that are city names and print the 3rd element

# to loop in an array you should use:
for x in fruits:    # this will print all the elements in fruits
  print(x)

for e in range(0, len(fruits)):
  print(fruits[0])

# To add more elements to the end of the array you use .append or .insert
fruits.append('grapes')
fruits.insert('plums')

# To delete an element from the array use .pop and specify the index number
fruits.pop(0) # this will remove the first element from the array. if you do not specify any index number, it will automatically delete the last element in the array.

# You can also use .remove to remove an element from the array but yu should also specify which element to delete
fruits.remove('grapes') # this will remove 'grapes' from the array



