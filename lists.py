
courses = ['History', 'Math', 'Physics', 'CompSci']

print(courses[3]) # [] is an index. Starts at 0.

print(courses[-1]) # negative numbers start at the end of the list
                   # useful if you just want the last number in list

print(courses[0:2]) #includes the first number (0) but stops before the second number (2)

print(courses[2:]) #starts at index 2 and lists all values after
                    #called slicing

#list methods:

#append method: adds value to the end of something

courses.append('Art')

print(courses)


#insert method: to add value to a specific location (index, 'value')

courses.insert(0, 'Art')

print(courses)


#extend method: when you want to add multiple values to lists
courses = ['History', 'Math', 'Physics', 'CompSci']
courses_2 = ['Art', 'Education']

courses.extend(courses_2)

print(courses)


#remove method: remove values from lists

courses = ['History', 'Math', 'Physics', 'CompSci']
courses.remove('Math')

print(courses)


#pop method: removes the last thing on the list (for a stack or a que)

courses = ['History', 'Math', 'Physics', 'CompSci']

popped = courses.pop() # can keep popping off values until list is empty

print(popped)
print(courses)


#reverse method: shows the list in reverse

courses = ['History', 'Math', 'Physics', 'CompSci']

courses.reverse()

print(courses)


#sort method: sorts list in alphabetical order

courses = ['History', 'Math', 'Physics', 'CompSci']

nums = [1, 5, 2, 4, 3]

courses.sort()
nums.sort() # numbers are attended to

print(courses)
print(nums)

                                                                                            
