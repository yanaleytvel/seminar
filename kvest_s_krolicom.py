import random
dl=10
zd=100
uv=20
ves=30


def poest_travu(zd, ves):
    a=int(input('Какой травы поесть? Жухлой - 0, Зелёной - 1 ', end='\n'))
    if(a==0):
        zd+=10
        ves+=15
        return zd, ves
    elif(a==1) and (uv<30):
        zd-=30
        print('Прости, но ты не можешь пройти на лужайку. У тебя недостаточно уважения:(')
        return zd, ves
    elif(a==1) and (uv>=30):
        zd+=30
        ves+=30
        return zd, ves

def kopat_noru(dl, zd):
    b=int(input('Как кролику нужно копать нору? Интенсивно - 1, Лениво - 0 ', end='\n'))
    if(a==1):
        dl+=5
        zd-=30
        return dl, zd
    elif (a==0):
        dl+=2
        zd-=10
        return dl, zd   

def draka_s_krolikami(ves, uv, zd):
    c=int(input('С кем ты будешь драться? Со слабым существом (ег вес может быть равен от 10 до 30) - 1, Со средним существом (его вес может быть равен от 40 до 60), С сильным существом (его вес может быть равен от 70 до 100)', end='\n'))
    if(c==1):
        k= random.choice([10, 20, 30])
        l = random.randint(0,k+ves)
        if(ves/k+ves>=l):
            zd+=10
            uv+=5
            print("Ура! Твой кролик победил своего соперника.")
        else:
            zd-=15
            uv-=10
            print("К сожалению твой кролик проиграл битву:(")
    elif(c==2):
        k= random.choice([40, 50, 60])
        l = random.randint(0,k+ves)
        if(ves/k+ves>=l):
            zd+=25
            uv+=20
            print("Ура! Твой кролик победил своего соперника.")
        else:
            zd-=35
            uv-=30
            print("К сожалению твой кролик проиграл битву:(")
    elif(c==3):
        k= random.choice([70, 80, 90, 100])
        l = random.randint(0,k+ves)
        if(ves/k+ves>=l):
            print("Ура! Твой кролик победил своего соперника.")
            zd+=30
            uv+=20
        else:
            zd-=30
            uv-=20
            print("К сожалению твой кролик проиграл битву:(")

def noch(dl, zd, uv, ves):
    dl-=2
    zd+=20
    uv-=2
    ves-=5
    return dl, zd, uv, ves

   
print("Добро пожаловать в игру! Сегодня тебе предстоит пройти квест игру, в которой ты будешь принимать решения за кролика.Изначально у тебя есть 4 основных параметра, длина норы - 10, здоровье - 100, уважение - 20 и вес - 30.Твоя задача добиться уважения больше 100 , при этом основные параметры не должны достигнуть нуля. Ночью кролик будет спать, и пока он отдыхает величина основных параметров будет изменяться. Длина норы будет уменьшаться  на 2 единицы, к здоровью прибавляется 20 единиц, уважение уменьшается  на 2 единицы, а  вес уменьшается на 5 единиц .Управление кроликом осуществляется в консоли. Желаю тебе приятной игры , можешь приступать",  end='\n')
while(dl>0) and (zd>0) and (uv>0) and (ves>0):
    a=int(input("Выберите действие, которое должен совершить ваш кролик, копать норку - 1, кушать травку - 2, пойти драться с другими кроликами - 3, лечь спать - 4"))
    if(a==1):
        dl,zd=kopat_noru(dl, zd)
        print("Фух, твой кролик неплохо постарался. Теперь твои основные параметры выглядят так: длина норы -" ,dl, "уважение -",uv,"здоровье -",zd,"и вес-",ves)
    elif(a==2):
        zd,ves=poest_travu(zd, ves)
        print("Ура! Твой кролик сыт и готов играть дальше! Теперь твои основные параметры выглядят так: длина норы -" ,dl, "уважение -",uv,"здоровье -",zd,"и вес-",ves)
    elif(a==3):
         ves,uv,zd=draka_s_krolikami(ves,uv, zd)
         print("Это было нелегко, но так весело!Теперь твои основные параметры выглядят так: длина норы -" ,dl, "уважение -",uv,"здоровье -",zd,"и вес-",ves)
    elif(a==4):
        dl,zd,uv,ves=noch(dl,zd,uv,ves)
        print("Наступила ночь, твой кролик очень устал, ему нужно хорошенько выспаться, чтобы завтра,с новыми силами, покорять мир кроликов!")

if(uv>100):
    print("Поздравляю, ты выйграл!")
else:
    print("К сожалению ты проиграл:(Попробуй ещё разок")
