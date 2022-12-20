names = ["Sanjay", "Ramesh", "Suresh", "Ravi"]
nums = [1,2,3]
#Join two lists
#names.extend(nums)
#print(names)
#Sort the list
names.sort()
print(names)
#Append the name "Ravi" to the list
names.append("Ravi")
print(names)
#Append the name "Ravi" to the list
mixed = names.copy()
print(mixed)
#Clear the list names
names.clear()
print(names)
#Reverse the list
mixed.reverse()
print(mixed)
#Remove the element "suresh"
mixed.pop(1)
print(mixed)
#remove the element at index 4
mixed.pop(3)
print(mixed)
#Insert an element "Raja" and index 3
mixed.insert(3,"Raja")
print(mixed)

