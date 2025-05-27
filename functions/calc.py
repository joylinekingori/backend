def add(a,b):
    answer=a+b
    return answer

def multiply(a,b):
    result=a*b
    return result
def divide(a,b):
    result=a/b
    return result
def modulus(a,b):
    result=a%b
    return result
def exponential3(a,b):
    result=a**b
    return result
def square(a):
    result=a**2
    return result

def cube(b):
    result=b**3

def sum(*numbers):
    total=0
    for number in numbers:
        total+=numbers
    return total

def power(base, exponent=3):
    return base ** exponent
def sum (* numbers):
    total=0
    for number in numbers:
        total+= number
    return total


def exam_results(*args, **kwargs):
    name = kwargs.get('name')
    course = kwargs.get('course')
    if len(args) == 0:
        print(f"Hello {name}, we don't have your results for {course}")
    elif len(args) == 1:
        print(f"Hello {name}, your average score for {course} is {args}")
    else:
        sumtotal = 0
        for score in args:
            sumtotal += score
        average = sumtotal / len(args)
        print(f"Hello {name}, your average score for {course} is {average}")
        
def find_even(stop):
    start = 10
    while start <= stop:
        if start % 2== 0:
            print (start)
    start += 1
    # continue
    # print(f"{start} is even")


    






