import csv
import math
import time

# Создаем CSV-файл и задаем кодировку
with open('temperature_data.csv', mode='w', encoding='utf-8', newline='') as file:
    writer = csv.writer(file)

    # Записываем заголовки
    writer.writerow(['Время', 'Датчик 1 (°C)', 'Датчик 2 (°C)'])

    # Начальные температуры
    initial_temperature_sensor1 = 45.0
    initial_temperature_sensor2 = 50.0

    # Время в секундах и общая длительность (200 секунд)
    current_time = 0
    total_duration = 200

    while current_time <= total_duration:
        # Рассчитываем температуры с плавными изменениями
        temperature_sensor1 = initial_temperature_sensor1 + 25.0 * math.sin(2 * math.pi * current_time / total_duration)
        temperature_sensor2 = initial_temperature_sensor2 + 20.0 * math.sin(2 * math.pi * current_time / total_duration)

        # Записываем данные в файл
        writer.writerow([current_time, temperature_sensor1, temperature_sensor2])

        # Увеличиваем текущее время
        current_time += 1
        time.sleep(0.1)  # Пауза в 0,1 секунды между записями