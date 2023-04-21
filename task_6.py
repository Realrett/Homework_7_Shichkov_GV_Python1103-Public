# Задача 36: Напишите функцию print_operation_table(operation, num_rows=6, num_columns=6),
# которая принимает в качестве аргумента функцию, вычисляющую элемент по номеру строки и столбца.
# Аргументы num_rows и num_columns указывают число строк и столбцов таблицы, которые должны быть распечатаны.
# Нумерация строк и столбцов идет с единицы (подумайте, почему не с нуля).
# Примечание: бинарной операцией называется любая операция, у которой ровно два аргумента, как, например, у операции умножения.
#
# *Пример:*
#
# **Ввод:** `print_operation_table(lambda x, y: x * y) `
# **Вывод:**
#
# 1 2 3 4 5 6
# 2 4 6 8 10 12
# 3 6 9 12 15 18
# 4 8 12 16 20 24
# 5 10 15 20 25 30
# 6 12 18 24 30 36

class DataTable:
    data = []
    num_rows = 0
    num_columns = 0

    def print_array(self):
        for i in self.data:
            for j in i:
                print(f"{j}", end=" ")
            print()

    def print_operation_table(self, operation, num_rows, num_columns):
        self.num_rows = num_rows
        self.num_columns = num_columns
        self.data.append([el + 1 for el in range(num_columns)])
        for el in range(1, num_rows):
            self.data.append([el + 1])
        for row in range(1, num_rows):
            for col in range(1, num_columns):
                numb = eval("lambda " + operation)
                self.data[col].append(
                    numb(self.data[col][0], self.data[row][0]))
        self.print_array()


obj = DataTable()
obj.print_operation_table("x, y: x * y", 6, 6)
