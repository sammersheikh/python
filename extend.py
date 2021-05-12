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
