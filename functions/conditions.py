def check_if_even(*number):
    for num in number:
        if num%2==0:
            print(f"{num}is even")
def check_even_or_odd(number):
    if number%2==0:
        print(f"{number} is even")
    else:
        print(f"{number} is odd")
# def check_divisibility(n):
#     for x in range(1,n+1):
#         if x%2==0:
#             print(f"{x} is divisible by 2")
#         elif x%3==0:
#             print(f"{x} is divisile by 3")
#         elif x%5==0:
#             print(f"{x} is divisible by 5")
#         else:
#             print(f"{x} is not divisible by 2,3,5")
def check_divisibility(n):
    for x in range(1,n+1):
        if x%2==0:
            print(f"{x} is divisible by 2")
        elif x%3==0:
            print(f"{x} is divisile by 3")
        elif x%5==0:
            print(f"{x} is divisible by 5")
        else:
            print(f"{x} is not divisible by 2,3,5")


def fizz_buzz(n):
    for x in range(1,n+1):
        if x%3==0:
            print("Fizz")
        elif x%5==0:
            print("Buzz")
        elif x%3==0 and x%5==0:
            print("FizzBuzz")
        else:
            print(x)

def count_down(start):
    while start>=0:
        print(f"countdown at {start}")
        start -=1

def countdown_with_break(start,stop):
    while start>=0:
        print(f"count down at {start}")
        if start==stop:
            print(f"stopping at {stop}")
            break
        start-=1
def countdown_with_odd(start):
    while start>=0:
        if start%2==0:
            start-=1
            continue
        print(f"countdown at {start}")
        start-=1

def even_numbers():
    even=0
    while even<=100:
        if even%2!=0:
            even+=1
            continue
        print({even})
        even+=1


