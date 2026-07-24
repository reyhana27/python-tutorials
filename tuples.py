#tuples are used to store multiple items in a list that cannot be changed after created.
#no modifications can be made to the tuples.
threesiblings = ('lola', 'lily', 'linda') #this is a tuple
print(threesiblings)

#tuples are also indexed starting from 0 and they have a stable order that cannot be changed
#tuples can have items with the same value
food = ('cake', 'cake', 'chips')  #this tuple contains duplicate values

print(len(threesiblings)) #prints the length of the tuple

#to create a tuple with only one item, add a comma after the item.
cake = ('chocolate',)

#tuples can be strings, integers, and, booleans
#tuples can also be a mix of strings, integers, and, booleans

#to print the datatype of a tuple:
print(type(food))

#similar to arrays, you can refer to certain elements in tuples by using index numbers and also the '-1' for the last element then '-2' for the second to last element and so on.

#you can specify the range of which elements in a tuple to be printed
foody = ('cake', 'pie', 'burger', 'fries', 'chicken')
print(foody[1:3])  #this will print out the second, third, and, fourth element of the tuple

#you can leave out certain selement from the tuple by:
foody = ('cake', 'pie', 'burger', 'fries', 'chicken')
print(:2)  #this will print out all the elements but will leave out burger which is at index 2

#you can print out all elements of a tuple starting from a certain element
foody = ('cake', 'pie', 'burger', 'fries', 'chicken')
print(foody[1:]) #this will print out all the elements in the tuple starting from 'pie'

#you can specify negative indexes to start the search from the right side,
foody = ('cake', 'pie', 'burger', 'fries', 'chicken')
print(foody[-4:-1]   #prints out items from index -4 which is included until -1 which is excluded

#to check if an item exists in a tuple:
foody = ('cake', 'pie', 'burger', 'fries', 'chicken')
if 'pie' in foody:
  print('yes it exists')  #prints out 'yes it exists' if 'pie' is in the tuple




