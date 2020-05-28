sum_1 = 0
p_1 = 1
sum_2 = 0
p_2 = 1
count = 0
q = 0
with open("first_2.txt", 'rb') as f, open("second_2.txt", 'wb') as g:  # працюємо з двома текстовими файлами
    for item in f:  # цикл обходу множини, нижче формули
        q -= 1
        last_element = float(item)
        sum_1 += float(item)
        p_1 *= float(item)
        sum_2 += (float(item))
        p_2 *= float(item)
        a = p_2
        count += 1

with open("first_2.txt", 'rb') as f, open("second_2.txt", 'wb') as g:  # працюємо з двома текстовими файлами
    for item in f:  # цикл обходу множини

        s = "Сума чисел = " + str(sum_1) + "\n"  # конвертування float => str
        bt = s.encode()  # конвертування str=>bytes
        g.write(bt)  # записування bt у файл

        s = "Сума квадратів чисел = " + str(sum_2) + "\n"  # конвертування float => str
        bt = s.encode()  # конвертування str=>bytes
        g.write(bt)  # записування bt у файл

        s = "Добуток чисел = " + str(p_1) + "\n"  # конвертування float => str
        bt = s.encode()  # конвертування str=>bytes
        g.write(bt)  # записування bt у файл

        s = "Квадрат добутку чисел = " + str(a) + "\n"  # конвертування float => str
        bt = s.encode()  # конвертування str=>bytes
        g.write(bt)  # записування bt у файл

        s = "Останній компонент файлу = " + str(last_element)  # конвертування float => str
        bt = s.encode()  # конвертування str=>bytes
        g.write(bt)  # записування b у файл
        break
