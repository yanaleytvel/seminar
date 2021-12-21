def uchastnik():
    ff = {}
    while True:
        try:
            familia, name, ocenka = map(str, input().split())
            ff[familia + ' ' + name] = ocenka
        except ValueError:
            return(ff)


n = int(input('Введите количество олимпиад: '))
Olimpiads = [0] * n
for i in range(n):
    Olimpiads[i] = uchastnik()

f = set
for i in range(n):
    f = f.union(set(Olimpiads[i].keys()))
print(len(f))

DiktionaryPoNomeram ={}
i = 1
for n in f:
    DiktionaryPoNomeram[str(i) + "_" + n[0] + "_" + str(len(n.split()[1]))]= n
    i += 1
print(DiktionaryPoNomeram)

ChUch3 =set(Olimpiads[0].keys())
for i in range(len(Olimpiads)):
    ChUch3 =ChUch3.intersection(Olimpiads[i].keys())
print(len(ChUch3))