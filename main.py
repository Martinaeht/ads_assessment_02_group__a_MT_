"""
Simple Calculator
"""
# Provide your solution here

def calculate(integer1:int, operator:str, integer2:int):
    if operator == "+":
        return(integer1 + integer2)
    elif operator == "-":
        return (integer1 - integer2)
    elif operator == "*":
        return (integer1*integer2)
    elif operator == "/":
        if integer2 != 0:
            return (integer1/integer2)
        elif integer2 == 0:
            print("Division by 0 is not allowed")
    else:
        print("Invalid operator.")

result = calculate(21, "+", 3)
print(result)



"""
Reverse Word
"""
# Provide your solution here

i = 0
def reverse_word(word:str):
    for i in range(len(word)):
        print(word.capitalize()[len(word) - 1 - i])

reverse_word("green")

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("Test your functions by calling them here. Use different parameter values to test them with different scenarios.")

