import numpy as np

def random_predict(number:int=1) -> int:
    """Рандомно угадываем число

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    
    count = 0
    # переманные для randint которые будут меняться в зависимости от условия
    a = 1
    b = 101
    # Бесконечный цикл до выполнения условия
    while True:
        count += 1
        predict = np.random.randint(a, b) # предпологаемое число
        # Регулирование зоны поиска np.random.randint(a, b) 
        if number > predict:
            a = predict
        elif number < predict:
            b = predict + 1
        elif number == predict:
            break # Выход из цикла, если угадали
    # Возвращение количества попыток
    return count

def score_game(random_predict) -> int:
    """За какое количество попыток в среднем из 1000 подходов
угадывает наш алгоритм
    
    Args:
        random_predict([type]): функция угадывания
    returns: среднее количество попыток
    """
    count_ls = [] # список для сохранения количества попыток
    np.random.seed(1) # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000)) # загадали список чисел
    for number in random_array:
        count_ls.append(random_predict(number))
    score = int(np.mean(count_ls)) # находим среднее количество попыток
    
    
    print(f'Ваш алгоритм угадывает число в среднем за: {score} попыток')
    return(score)

# RUN
if __name__ == '__main__':
    score_game(random_predict)
        