import random
popitka=0
zagadannoe_chislo=random.randint(1,30)
print("Привет, друг! Предлагаю тебе немножко поиграть:) Я загадаю число от 1 до 30 (включительно) и дам тебе 7 попыток, а ты попытаешься угадать, число которое я загадал.")
while popitka<7:
    chislo_igroka=int(input("Пожалуйста, введи число: "))
    popitka+=1
    if chislo_igroka>zagadannoe_chislo:
        print("Неправильно! Загаданное число меньше,чем твое. Попробуй ещё разок:)")
    if chislo_igroka<zagadannoe_chislo:
        print("Неправильно! Загаданное число больше,чем твое. Попробуй ещё разок:)")
    if chislo_igroka==zagadannoe_chislo:
        break
if chislo_igroka==zagadannoe_chislo:
    print("Поздравляю, у тебя получилось отгадать число! Ты победил!!!")
else:
    print("К сожалению, ты не угадал число и проиграл(. Если тебе интересно, я загадал число {0}".format(zagadannoe_chislo))


    
 