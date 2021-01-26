def loe_failist(f):
    fail=open(f,'r',encoding='utf-8-sig')
    mas=[]
    for rida in fail:
        mas.append(rida.strip())
    fail.close()
    return mas
def salvesta_failisse(f,text):
    fail=open(f,'a',encoding="utf-8-sig")
    fail.write(text+"\n")
    fail.close()
    mas=[]
    mas=loe_failist(f)
    return mas
def tolkimine(rus_list,est_list):
    slovo=input("Введите слово для перевода:")
    if slovo in rus_list:
        ind=rus_list.index(slovo)
        print(f"{slovo}-{eng_list[ind]}")
    elif slovo in eng_list:
        ind=eng_list.index(slovo)
        print(f"{slovo}-{rus_list[ind]}")
    else:
        print("f{slovo.upper()} отсутсвует в словаре")
rus_list=loe_failist("rus.txt")
eng_list=loe_failist('eng.txt')
print(rus_list)
print(eng_list)
while True:
    v=input('Перевод-1, Новое слово-2, Исправить ошибку-3, Проверка знаний-4')
    if v=='1':
        tolkimine(rus_list,eng_list)
    elif v=='2':
        rus_sona=input("Введи слово на русском:")
        eng_sona=input("Введи слово на английском:")
        rus_list=salvesta_failisse("rus.txt",rus_sona)
        eng_list=salvesta_failisse("eng.txt",eng_sona)
        print(rus_list)
        print(eng_list)
