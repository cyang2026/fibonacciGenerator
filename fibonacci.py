print("Hello, this is a fibonacci sequence generator!")
print("All you have to do is to enter the number of digits you want this program to generate it to, and I will automatically generate the numbers for you!")
print("The maximum for this program is 1000 digits.")
while(True):
    answer = input()
    if answer > 1000:
        print("Sorry, that is over the maximum for this program!")
    elif answer < 0:
        print("Sorry, I can't generate a negative amount of digits!")
    else:
        break

def fibonacci(digits):
    result = [0, 1]
    while(len(result) <= digits):
        if len(result) == 1:
            result.append(1)
        else:
            result.append(result[-1] + result[-2])
    print(result)
fibonacci(answer)
