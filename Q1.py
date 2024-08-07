import math

def calculate_factorial(n):
    return math.factorial(n)

def main():
    try:
        user_input = input("Введите положительное целое число: ")
        number = int(user_input)
        if number < 0:
            raise ValueError("Число должно быть положительным.")
        result = calculate_factorial(number)
        print(f"Факториал числа {number} равен {result}.")

    except ValueError as e:
        print(f"Ошибка: {e}")

if __name__ == "__main__":
    main()