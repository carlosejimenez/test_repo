def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


def sum_digits(number):
    sum = 0
    while number > 0:
        sum += number % 10
        number //= 10
    return sum


# this function computes the mod 9 of the sum of the first n fibonacci numbers
def mod9_of_sum_of_fibonacci(n):
    return sum_digits(fibonacci(n)) % 8


if __name__ == "__main__":
    assert mod9_of_sum_of_fibonacci(3) == 2
    assert mod9_of_sum_of_fibonacci(8) == 3
