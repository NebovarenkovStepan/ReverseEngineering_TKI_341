def bubble_sort(arr):
    """Функция пузырьковой сортировки."""
    n = len(arr)
    for i in range(n - 1):
        swapped = False
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                # В Python обмен значений делается в одну строку
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break

def get_numbers():
    """Функция для ввода чисел с проверкой корректности."""
    n = 0
    while True:
        try:
            user_input = input("Введите количество чисел: ")
            n = int(user_input)
            if n > 0:
                break
            else:
                print("Некорректный ввод. Введите положительное целое число.")
        except ValueError:
            print("Некорректный ввод. Введите положительное целое число.")

    numbers = []
    print(f"Введите {n} чисел (по одному в строке):")
    
    for i in range(n):
        while True:
            try:
                user_input = input(f"Число {i + 1}: ")
                num = float(user_input)
                numbers.append(num)
                break
            except ValueError:
                print("Некорректный ввод. Введите число.")
    
    return numbers

def main():
    # В Python 3 проблем с кодировкой (как SetConsoleCP в C++) обычно нет,
    # строки по умолчанию в Unicode.
    
    nums = get_numbers()

    # Вывод исходного массива. 
    # *nums распаковывает список, sep=" " задает разделитель пробел
    print("\nИсходный массив:", end=" ")
    print(*nums, sep=" ")

    bubble_sort(nums)

    print("Отсортированный массив:", end=" ")
    print(*nums, sep=" ")

    print("\nНажмите Enter для выхода...")
    input()

if __name__ == "__main__":
    main()