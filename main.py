# Решение задачи:
# 1. Сгенирировать колоду карт, добавив к каждой карте МАСТЬ
# 2. Перемишать колоду используя метод shuffle()
# 3. Через функ getCards() - выдать карти с кололды, при этом функц getCards() возвращает СПИСОК карт, для того чтобы  можно было подсчитать сумму очков и при этом изменить к-во очков если выпадет А - ТУЗ в пользу игрока
# 4. Через функц. sumCards() подсчитать сумму очков. 
# 5. В функции sumCards() происходит перебор каждой карты и отделение масти от числа через функц getNumber(), далее происходит поиск А - ТУЗА и если он найден ТУЗ перезаписывается в конец списка что бы правильно(в пользу игрока) присвоить значение 1 или 11. Если в списке два туза и более принять значение для ТУЗА - 1(через метод count('A')).задачи
# 6. Через циклы WHILE организовать ввыдачу карт ИГРОКУ и ДИЛЛЕРУ

# Вызов метода shuffle() - для перетасовки карт
from random import shuffle

# создание колоды карт
deck = []
for j in range (1,5):
    match j:
        case 1:
            suits = '\u2660'
        case 2:
            suits = '\u2663'
        case 3:
            suits = '\u2666'
        case 4:
            suits = '\u2665'
            
    cards1 = [f"{i} {suits}"for i in range(2,11)]
    deck.extend(cards1)
    deck.extend([f'K {suits}', f'Q {suits}', f'J {suits}', f'A {suits}'])


# линейный поиск для поиска тузов в раздачи МОЖНО использовать метод строк find() 
def linearSearch(_list,key):
    for i in range(len(_list)):
        if _list[i] == key:
            return i
    return -1    

# функция выдачи карт с колоды
def getCards(deck, n):
    listPlayerDealer = []
    for i in range(0,n):
        listPlayerDealer.append(deck.pop())
    return listPlayerDealer

# функц обаработки карты (отделяет номинала от масти) 
def getNumber(CardWithoutSuit):
    i = CardWithoutSuit.find(' ')
    return CardWithoutSuit[:i:] #возвращает все что находится до пробела чтобы отделлить масть от номинала


# функция опредиление суммы очков ИГРОКА
def sumCards(listPlayer):

    newList = [] # список розданных карт без МАСТИ
    for j in listPlayer:
        el1 = getNumber(j) 
        newList.append(el1)
    temp  = linearSearch(newList,'A') # поиск ТУЗА
    if not temp == -1:
        ase = newList.pop(temp)
        newList.append(ase) # если туз найден он переставляется в конец списка

    sum = 0
    for el in newList: 
        if el == 'K' or el == 'Q' or el == 'J':
            el = 10
        elif el == 'A':
            if sum + 11 <= 21 and newList.count('A') < 2:
                el = 11
            else:
                el = 1
        sum += int(el)
    return sum

# функция опредиление суммы очков ДИЛЛЕРА (отличается уловием для ТУЗА: - А=11 если сумма очков больше 21 во всех остальных случаях А=1 - ТО ЕСТЬ КАРТЫ ДИЛЛЕРА ИЗМ. В ПОЛЬЗУ ИГРОКА)
def sumCardsDealer(listPlayer):

    newList = [] # список розданных карт без МАСТИ
    for j in listPlayer:
        el1 = getNumber(j) 
        newList.append(el1)
    temp  = linearSearch(newList,'A') # поиск ТУЗА
    if not temp == -1:
        ase = newList.pop(temp)
        newList.append(ase) # если туз найден он переставляется в конец списка

    sum = 0
    for el in newList: 
        if el == 'K' or el == 'Q' or el == 'J':
            el = 10
        elif el == 'A':
            if sum + 11 > 21:
                el = 11
            else:
                el = 1
        sum += int(el)
    return sum

arr1 = [] # карты игрока
arr2 = [] # карты диллера

# Перетасовка колоды
shuffle(deck)

print("ИГРА НАЧАЛАСЬ")

# ПЕРВАЯ выдача карт игроку
arr1 = getCards(deck,2)
print(f"Выдача игроку {arr1}")

# вывод суммы очков ИГРОКА
print(sumCards(arr1))

if sumCards(arr1) == 21:
    print("Вы выиграли")
else:
    m = int(input("взять карту (ЕЩЕ) введите - 1 отмена (ХВАТИТ) введите - 0 = "))
    # следующая выдача карт ИГРОКУ
    while m == 1:
    
        arr1.extend(getCards(deck,1))
        print(f"Выдача игроку {arr1}")
        print(sumCards(arr1)) 

        if sumCards(arr1) > 21:
            print("Вы проиграли")
            break
        elif sumCards(arr1) == 21:
            print("Вы выиграли")
            break
        m = int(input("взять карту (ЕЩЕ) введите - 1 отмена (ХВАТИТ) введите - 0 = "))
    
# выдача карт ДИЛЛЕРУ    
while sumCards(arr1) < 21:

    arr2.extend(getCards(deck,1))

    print(f"Выдача диллеру {arr2}")
    print(sumCardsDealer(arr2))

    if sumCardsDealer(arr2) > sumCards(arr1) and sumCardsDealer(arr2) <= 21:
        print("Диллер выиграл")
        break
    elif sumCardsDealer(arr2) > 21:
        print("Диллер проиграл")
        break
    elif sumCardsDealer(arr2) == sumCards(arr1): 
        print("ничья")
        break
