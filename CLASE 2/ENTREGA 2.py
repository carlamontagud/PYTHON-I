#Exercise 1: FizzBuzz
#1. Write a FizzBuzz Function: Create a function fizzbuzz(n) that takes an integer n as a parameter. 
#2. Implement FizzBuzz Logic: The function should print: ○ 
#- "Fizz" for multiples of 3 
#- "Buzz" for multiples of 5 
#- "FizzBuzz" for multiples of both 3 and 5 
#- The number itself for other numbers 
#3. Call the Function: Call the function for numbers 1 to 20.
def fizzbuzz(n):
    for i in range(1, n+1):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)

fizzbuzz(20)
#Exercise 2: Basic Data Filtering
#1. Create a List of Mixed Data Types: Create a list that contains a mix of integers, strings, and floats. 
#2. Filter the List: Use list comprehension to create a new list that contains only the integers from the original list. 
#3. Print the New List: Output the filtered list of integers.1. Create a List of Mixed Data Types: Create a list that contains a mix of integers, strings, and floats. 
mixed_list = [1, "Carla", 3.14, 42, "car", 99, 7.5, "university", 8]
integers_only = [item for item in mixed_list if isinstance(item, int)]
print(integers_only)
#Exercise 3: Simple To-Do List
#1. Create an Empty List: Start with an empty list called todo_list. 
#2. Define Functions: 
#- A function add_task(task) that adds a task to the list. 
#- A function show_tasks() that prints all tasks in the list.
todo_list = []
def add_task(task):
    todo_list.append(task)
    print(f'Task "{task}" added.')

def show_tasks():
    if not todo_list:
        print("No tasks in the list.")
    else:
        print("To-Do List:")
        for index, task in enumerate(todo_list, 1):
            print(f"{index}. {task}")

add_task("Finish Python assignment")  
add_task("Go for a run")              
show_tasks()  
#Exercise 4: Temperature Converter
#1. Define a Conversion Function: Write a function celsius_to_fahrenheit(celsius) that converts Celsius to Fahrenheit. 2. 
#2. Print the Result: Output the converted temperature for 22ºF, 46ºF, 51ºF and 76ºF.
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

celsius_temperatures = [22, 46, 51, 76]

for temp in celsius_temperatures:
    fahrenheit = celsius_to_fahrenheit(temp)
    print(f"{temp}ºC is equal to {fahrenheit}ºF")