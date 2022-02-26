# Первый способ - нативный.

def Stepen1(N):
    if N < 1:
        return 0
    x = 1
    current = 2
    while N > current:
        current *= 2
        x += 1
    return x

# Второй способ - используя бинарное представление чисел.
# В бинарном представлении числа его самая старшая единица - это ближайшая к числу "снизу" степень двойки.
# Тогда ближайшая "сверху" степень двойки - это следующий разряд.
# пример: число N=5 в двоичном виде - 101. Ближайшая к нему степень двойки "снизу", то есть которая меньше него - это число 2*2 = 4 (100)
# Тогда ближайшая "сверху" степень двойки - 2**3 = 8 (1000)  его длина на 1 больше чем показатель степени и также на 1 больше чем длина исходного числа
# Получается что искомая степень двойки числеенно равна длине битового представления числа N
# Не забываем, что в двоичном числе первые 2 символа - служебные,"0b"

def Stepen2(N):
    if N < 1:
        return 0                        # частный случай
    Nstring = str(bin(N))
    Nstring = Nstring[2:]               # отрезаем два служебных символа
    return len(Nstring)                 # 




import unittest

class Tests_Stepen(unittest.TestCase):

        
    def test_1_Stepen1(self):
        args = [513, 0, 1, 25, 3, 127]
        results = [10, 0, 1, 5, 2, 7, ]
        for i in range(5):
            self.assertEqual(Stepen1(args[i]), results[i])

    def test_2_Stepen2(self):
        args = [513, 0, 1, 25, 3, 127]
        results = [10, 0, 1, 5, 2, 7, ]
        for i in range(5):
            self.assertEqual(Stepen2(args[i]), results[i])
        
if __name__ == '__main__':
    try: unittest.main()
    except SystemExit: pass
