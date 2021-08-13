def fizz_buzz(numb):
    if numb % 3 == 0 and numb % 5 == 0:
        return 'FizzBuzz'
    elif numb % 3 == 0:
        return 'Fizz'
    elif numb % 5 == 0:
        return 'Buzz'
    else:
        return numb

n, b = input('Input range').split()
while True:
    try:
        n = int(n)
        b = int(b)
    except ValueError:
        print('No letters')
    if n >= b:
        print('Again')
    else:
        break
    n, b = input("Input range").split()
    n = int(n)
    b = int(b)
b = b + 1
for numb in range(n, b):
    print(fizz_buzz(numb))