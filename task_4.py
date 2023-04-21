# Задание 4.
# Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса
# (метод init()), который должен принимать данные (список списков) для формирования матрицы.
# Подсказка: матрица — система некоторых математических величин, расположенных в
# виде прямоугольной схемы.
# Примеры матриц: 3 на 2, 3 на 3, 2 на 4.

# 31 22
# 37 43
# 51 86

# 3 5 32
# 2 4 6
# -1 64 -8

# 3 5 8 3
# 8 3 7 1

# Следующий шаг — реализовать перегрузку метода str() для вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода add() для реализации операции сложения двух
# объектов класса Matrix (двух матриц). Результатом сложения должна быть новая матрица.
# Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой
# строки первой матрицы складываем с первым элементом первой строки второй матрицы и т.д.



class Matrix:
    def __init__(self, user_list):
        self.data = user_list
        self.rows = len(user_list)
        self.cols = len(user_list[0])

    def __str__(self):
        res = ""
        for row in self.data:
            for el in row:
                res += f"{el} "
            res += "\n"
        return res

    def __to_list(self):
        res = []
        for row in self.data:
            for el in row:
                res.append(el)
        return res

    def __add__(self, other):
        arr1 = self.__to_list()
        arr2 = other.__to_list()
        res_rows = self.rows if self.rows > other.rows else other.rows
        res_cols = self.cols if self.cols > other.cols else other.cols
        arr_sum = []
        res_matrix = []
        count = 0
        for i in range(len(arr1)):
            try:
                arr_sum.append(arr1[i] + arr2[i])
            except IndexError:
                arr_sum.append(arr1[i])
        for rows in range(res_rows):
            inner = []
            for cols in range(res_cols):
                inner.append(arr_sum[count])
                count += 1
            res_matrix.append(inner)
        return Matrix(res_matrix)


obj = Matrix([[31, 22], [37, 43], [51, 68]])
obj2 = Matrix([[31, 22], [37, 43]])

print(obj + obj2)
