# -*- coding: utf-8 -*-
"""
Класс Танк для игры.
"""
import random

class Tank:
    """
    Класс объекта танка

    :param model: название модели
    :type model: str
    :param min_damage: минимальный возможный урон для генератора
    :type min_damage: int
    :param max_damage: максимальный возможный урон для генератора
    :type max_damage: int
    :param health: количество здоровья танка
    :type health: int
    """
    def __init__(self, model: str, armor: int, min_damage: int, max_damage: int, health: int, is_player: bool = False):
        self.model : str = model
        self.armor : int = armor
        self.damage : int = random.randint(min_damage, max_damage)
        self.health : int = health
        self.is_player : bool = is_player
        self.is_alive : bool = True

    def print_info(self):
        """
        Метод для вывода информации о танке.
        """
        if self.is_alive:
            print(f"{self.model} имеет лобовую броню {self.armor} мм. при {self.health} ед. здоровья и урон в {self.damage} единиц")

    def shot(self, enemy) -> int:
        """
        Метод для стрельбы по врагам. Принимает входными данными экземпляр класса Tank

        :param enemy: враг
        :type enemy: Tank
        """
        enemy.health_down(self.damage)
        if enemy.health <= 0:
            print(f"{self.model}: Экипаж танка {enemy.model} уничтожен")
            enemy.is_alive = False
        else:
            print(f"{self.model}: Точно в цель, у противника {enemy.model} осталось {enemy.health} единиц здоровья")

    def health_down(self, damage: int):
        """
        Метод для получения урона. Принимает значение урона вражеского танка

        :param damage: вражеский урон
        :type damage: int
        """
        self.health = self.health - damage / self.armor
        if self.is_player:
            if self.health > 0 :
                print(f"{self.model}: Командир, по экипажу {self.model} попали, у нас осталось {self.health} очков здоровья")
            else:
                print(f"{self.model}: Командир, экипаж {self.model} уничтожен")
                exit(0)