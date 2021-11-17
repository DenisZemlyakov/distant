#создаём функцию
def passautomat():
    """пароль создаётся машиной
    """
    str0=".,:;!_*-+()/#¤%&"
    str1 = '0123456789'
    str2 = 'qwertyuiopasdfghjklzxcvbnm'
    str3 = str2.upper() # 'QWERTYUIOPASDFGHJKLZXCVBNM'
    print(str3) # 'QWERTYUIOPASDFGHJKLZXCVBNM'
    str4 = str0+str1+str2+str3
    print(str4)
    ls = list(str4) #список [".",]
    print(ls)
    random.shuffle(ls) #перемешаем значение
    print(ls)
# Извлекаем из списка 12 произвольных значений
psword = ''.join([random.choice(ls) for x in range(12)])
# Пароль готов
print(psword)
