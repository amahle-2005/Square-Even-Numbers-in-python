numbers = [1]

def get_numbers():
    while True:
        value = input("Enter number (press enter to exit/finish): ")
        if value == "":
            break
        try:
            value = int(value)
            numbers.append(value)
        except:
            raise ValueError(f"Invalid type: '{value}' ({type(value).__name__})- only int is allowed \nTry again: ")
        
    return numbers
def square_eve_numbers(numbers):
    return list(map(lambda x: x**2, filter(lambda x: x % 2 == 0, numbers)))

get_numbers()
print(square_eve_numbers(numbers))
#explanationn
# list() returns a list of what is entered inside if empty an empty list will be created
# map(lambda, data structure) applies the lambda expression to each value in a data structure
# filter(lambda, data structure) filters out numbers do not meet the requirement specified by lambda expression
# squares = list(map(lambda expression, data structure))
# Therefore we start with filter(lambda x: x%2 == 0, numbers) then we get all even numbers
# Then it is turned into a list, then map() is called, it applies the expression to all the values in a list.
# Then the last list is stored in squares.