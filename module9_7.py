def is_prime(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)

        # Функция для проверки простоты числа
        def is_prime_number(num):
            if num <= 1:
                return False
            for i in range(2, int(num**0.5) + 1):
                if num % i == 0:
                    return False
            return True

        if is_prime_number(result):
            print("Простое")
        else:
            print("Составное")

        return result

    return wrapper

@is_prime
def sum_three(a, b, c):
    return a + b + c

# Пример использования
result = sum_three(4, 2, 1)
print(result)
