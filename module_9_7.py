def is_prime(func):
    def wrapper(*args):
        result = func(*args)
        is_prime = False
        for i in range(2, result):
            if result % i == 0:
                is_prime = True
        if is_prime:
            print('Составное')
        else:
            print('Простое')
        return result
    return wrapper
@ is_prime
def sum_three(*args):
    return sum(args)

result = sum_three(2, 3, 6)
print(result)