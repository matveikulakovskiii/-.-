spisk=[] #tühi kiri
numbers=[1,2,3,4,5]
abc=["A","B","C"]
sõna="Programmeerimine"
sõna_list=list(sõna)
print(sõna)
print(sõna_list)
print(numbers)
while True:
    print("1-lisada täht kirrise ")
    print("1-lisada täht kirrise ")
    valik=int(input())
    if valik==1:
        a=input("sissesta täht")
        sõna_list.append(a)
        print(f"lisasime {a} uue kiri",sõna_list)
    elif valik==2:
        sõna_list.extend(abc)
        print(sõna_list)
    elif valik==3:
        a=input("sissesta täht, nis tahad lisada")
        i=input("sissesta numbri positsioon, kuhu tahad lisada täht")
        sõna_list.insert(i-1,a) #0,1,2...
        print(sõna_list)
    elif valik==4:
        a=input("sissesta täht, nis tahad lisada")
        sõna_list.count(a)
        sõna_list.remove(a)
        print(sõna_list)
print("na mne kodovij zamook a kakoi she parol?")
parol="poshel na kamaz"
parol1=list(parol)
print(parol1)
