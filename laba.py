swap1 = 0
srav = 0
arrpuz = []
arrvstavka = []
arrvibor = []
arrqs = []
arrshell = []



def puz(x):
    sr = 0
    sw = 0
    for i in range(len(x)):
        for j in range(len(x) - 1):
            sr += 1
            if x[j] > x[j + 1]:
                tmp = x[j]
                x[j] = x[j + 1]
                x[j + 1] = tmp
                sw += 1
    print("Пузырёк")
    print("Количество сравнений", sr, "Количество перестановок", sw)


def vstavka1(x):
    sw = 0
    sr = 0
    for i in range(1, len(x)):
        temp = x[i]
        tmp = i
        sr += 1
        while tmp > 0 and x[tmp - 1] > temp:
            x[tmp] = x[tmp - 1]
            tmp -= 1
            sw += 1
        x[tmp] = temp
    print("Вставками")
    print("Количество сравнений", sr, "Количество перестановок", sw)


def vibor(x):
    sw = 0
    sr = 0
    for i in range(len(x) - 1):
        mini = x[i]
        minindex = i
        for j in range(i + 1, len(x)):
            sr += 1
            if x[j] < mini:
                mini = x[j]
                minindex = j
                sw += 1
        x[i], x[minindex] = x[minindex], x[i]
    print("Выбором")
    print("Количество сравнений", sr, "Количество перестановок", sw)


def shell(x):
    sr = 0
    sw = 0
    step = len(x) // 2
    while step > 0:
        for i in range(len(x)):
            while i >= step:
                sr += 1
                if x[i] < x[i - step]:
                    x[i], x[i - step] = x[i - step], x[i]
                    sw += 1
                else:
                    break
                i -= step
        step //= 2
    print("Шелл")
    print("Количество сравнений", sr, "Количество перестановок", sw)


def qsort(x, nstart, nend):
    global srav, swap1
    if nstart >= nend:
        return
    L = nstart
    R = nend
    X = x[(L + R) // 2]
    while L <= R:
        srav += 1
        while x[L] < X:
            srav += 1
            L += 1
        while x[R] > X:
            R -= 1
            srav += 1
        srav += 1
        if L <= R:
            c = x[L]
            x[L] = x[R]
            x[R] = c
            L += 1
            R -= 1
            swap1 += 1
    qsort(x, nstart, R)
    qsort(x, L, nend)


def QS(x, start, finish):
    qsort(x, start, finish)
    print("Быстрая сортировка")
    print("Количество сравнений", srav, "Количество перестановок", swap1)

a = []
print("ПОЛНОСТЬЮ СОРТИРОВАННЫЙ СПИСОК")
for i in range(0, 10):
    a.append(i)
arrpuz = a.copy()
arrvstavka = a.copy()
arrvibor = a.copy()
arrqs = a.copy()
arrshell = a.copy()
puz(arrpuz)
vstavka1(arrvstavka)
vibor(arrvibor)
QS(arrqs, 0, len(arrqs) - 1)
shell(arrshell)
print()
print("ЧАСТИЧНО СОРТИРОВАННЫЙ СПИСОК")
b = []
for i in range(0, 5):
    b.append(i)
for i in range(10, 5, -1):
    b.append(i)
arrpuz = b.copy()
arrvstavka = b.copy()
arrvibor = b.copy()
arrqs = b.copy()
arrshell = b.copy()
puz(arrpuz)
vstavka1(arrvstavka)
vibor(arrvibor)
QS(arrqs, 0, len(arrqs) - 1)
shell(arrshell)
print()
print("ПОЛНОСТЬЮ НЕСОРТИРОВАННЫЙ СПИСОК")
c = []
for i in range(10,0,-1):
    c.append(i)
arrpuz = c.copy()
arrvstavka = c.copy()
arrvibor = c.copy()
arrqs = c.copy()
arrshell = c.copy()
puz(arrpuz)
vstavka1(arrvstavka)
vibor(arrvibor)
QS(arrqs, 0, len(arrqs) - 1)
shell(arrshell)


