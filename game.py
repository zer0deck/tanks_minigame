# -*- coding: utf-8 -*-
"""
Консольная текстова игра 'танчики'.
"""
import random
from os import system
from tank import Tank

def choose_tank_to_attack(attacking: Tank, enemy_dict: dict, player: Tank) -> str:
    """
    Функция для случайного выбора цели вражеского танка
    
    :param attacking: атакующий танк. Параметр нужен, чтобы танк не атаковал сам себя
    :type attacking: Tank
    :param enemy_dict: словарь со всеми врагами
    :type enemy_dict: dict
    :param player: экземпляр игрока
    :type player: Tank
    """
    goal_list = []
    for es in enemy_dict.values():
        if (es != attacking) & es.is_alive:
            goal_list.append(es)
    goal_list.append(player)
    goal = goal_list[random.randint(0, len(goal_list)-1)]
    return goal

def _string_to_bool() -> bool:
    """
    Техническая функция для конвертации строк в boolean значение
    """
    q = input("Создать врагов вручную (д/н)? ")
    if q == "д":
        return True
    elif q == "н":
        return False
    else:
        raise Exception("Ошибка. Введено неверное значение")

if __name__ == "__main__":

    p_model = input("Введите модель Вашего танка: ")
    p_min_damage, p_max_damage = map(int, input("Введите максимальный и минимальный урон для генерации (два числа через пробел): ").split())
    p_armor = int(input("Введите количество брони Вашего танка: "))
    p_health = int(input("Введите количество здоровья Вашего танка: "))
    player = Tank(model=p_model, armor=p_armor, min_damage=p_min_damage,
        max_damage=p_max_damage, health=p_health, is_player=True)

    enemy_amount = int(input("Введите количество врагов: "))
    enemy_dict = {}
    manualy_enemy_creation = _string_to_bool()

    for i in range(enemy_amount):
        if manualy_enemy_creation:
            e_model = input(f"Введите модель танка врага {i}: ")
            e_min_damage, e_max_damage = map(int, input("Введите максимальный и минимальный урон для генерации (два числа через пробел): ").split())
            e_armor = int(input(f"Введите количество брони танка врага {i}: "))
            e_health = int(input(f"Введите количество здоровья танка врага {i}: "))
            enemy_dict[e_model] = Tank(model=e_model, armor=e_armor, min_damage=e_min_damage,
                max_damage=e_max_damage, health=e_health)
        else:
            e_model = f"Враг_{i}"
            e_armor = random.randint(1, int(p_armor*1.25))
            e_health = random.randint(1, int(p_health*1.25))
            enemy_dict[e_model] = Tank(model=e_model, armor=e_armor, min_damage=p_min_damage,
                max_damage=p_max_damage, health=e_health)

    input("\nИгра создана. Нажмите ENTER для продолжения...")
    system('cls')

    while True:
        print("\n\t\tGame Table\n")
        player.print_info()
        for val in enemy_dict.values():
            val.print_info()
        
        attack = input("\nВведите модель врага для атаки: ")
        print()
        player.shot(enemy_dict[attack])
        for e in enemy_dict.values():
            destroyed = 0
            if e.is_alive:
                goal = choose_tank_to_attack(e, enemy_dict, player)
                e.shot(goal)
            else: 
                destroyed+=1

            if destroyed == len(enemy_dict):
                print("\nПобеда. Все враги уничтожены")
                exit(0)
        
        input("\nНажмите ENTER для продолжения...")
        system('cls')
            