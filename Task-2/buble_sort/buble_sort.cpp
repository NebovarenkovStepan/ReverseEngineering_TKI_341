#define NOMINMAX
#include <iostream>
#include <vector>
#include <algorithm>
#include <limits>
#include <Windows.h>

void bubbleSort(std::vector<double>& arr) {
    int n = (int)arr.size();
    for (int i = 0; i < n - 1; i++) {
        bool swapped = false;
        for (int j = 0; j < n - i - 1; j++) {
            if (arr[j] > arr[j + 1]) {
                std::swap(arr[j], arr[j + 1]);
                swapped = true;
            }
        }
        if (!swapped) break;
    }
}

std::vector<double> getNumbers() {
    std::vector<double> numbers;
    int n;

    std::cout << "Введите количество чисел: ";
    while (true) {
        if (std::cin >> n && n > 0) {
            break;
        }
        else {
            std::cout << "Некорректный ввод. Введите положительное целое число: ";
            std::cin.clear();
            std::cin.ignore((std::numeric_limits<std::streamsize>::max)(), '\n');
        }
    }

    std::cout << "Введите " << n << " чисел (по одному в строке):\n";
    for (int i = 0; i < n; i++) {
        double num;
        while (true) {
            std::cout << "Число " << (i + 1) << ": ";
            if (std::cin >> num) {
                numbers.push_back(num);
                break;
            }
            else {
                std::cout << "Некорректный ввод. Введите число:\n";
                std::cin.clear();
                std::cin.ignore((std::numeric_limits<std::streamsize>::max)(), '\n');
            }
        }
    }
    return numbers;
}

int main() {
    SetConsoleCP(1251);
    SetConsoleOutputCP(1251);

    std::vector<double> nums = getNumbers();

    std::cout << "\nИсходный массив: ";
    for (double x : nums) std::cout << x << " ";
    std::cout << std::endl;

    bubbleSort(nums);

    std::cout << "Отсортированный массив: ";
    for (double x : nums) std::cout << x << " ";
    std::cout << std::endl;

    std::cout << "\nНажмите Enter для выхода...";
    std::cin.ignore((std::numeric_limits<std::streamsize>::max)(), '\n');
    std::cin.get();

    return 0;
}