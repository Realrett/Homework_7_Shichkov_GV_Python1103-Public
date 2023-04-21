# Создать класс TrafficLight (светофор)
# и определить у него один приватный атрибут color (цвет) и публичный метод running (запуск).

# В рамках метода running реализовать переключение светофора в режимы:
# красный, желтый, зеленый. Продолжительность первого состояния (красный)
# составляет 7 секунд, второго (желтый) — 2 секунды, третьего (зеленый) —
# на ваше усмотрение.
# Для имитации "горения" каждого цвета испольщуйте ф-цию sleep модуля time

# Переключение между режимами должно осуществляться только
# в указанном порядке (красный, желтый, зеленый).

# Проверить работу примера, создав экземпляр и вызвав описанный метод.

from time import sleep


class TrafficLight:
    __color = ['red', 'yellow', 'green'];

    def running(self):
        print(self.__color[0])
        sleep(7)
        print(self.__color[1])
        sleep(2)
        print(self.__color[2])
        sleep(5)
        self.running()


obj = TrafficLight()
obj.running()