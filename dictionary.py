#dictionaries are used to store value in key:value pairs
#a dictionary is a collection that is ordered, changeable and does not allow duplicates
#dictionaries with curly brackets have keys and values
dictionary = {
  "name" : "rose"
  "age" : 20
  "eyecolor" : "brown"
}
print(dictionary)

#you can refer to dictionary values by using key names

dictionary = {
  "name" : "rose"
  "age" : 20
  "eyecolor" : "brown"
}
print(dictionary["age"])  #will print value for "age"

#2 values with the same key are not allowed. duplicates will overwrite existing values

#number of items in a dictionary:
print(len(dictionary))

#dictionary datatypes can be strings, integers, booleans and can have list datatypes

#type of items in a dictinoary
print(type(dictionary))

#dict method to make dictionary
info = dict(name = lila, age = 30, country = romania)

#get method to get value of a certain key
x = dictionary.get("age")

#.keys method to return all keys
z = dictionary.keys()

#.values method to get all values
y = dictionary.values()

#.items method to get all the key:value pairs
c = dictionary.items()

#check if a key exists
if "age" in dictionary:
  print("YES")  #prints "YES" if "age" is in dictionary

#update dictionary:
dictionary = {
  "name" : "rose"
  "age" : 20
  "eyecolor" : "brown"
}
dictionary.update({"age":33})


