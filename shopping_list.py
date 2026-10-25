goods_number = int(input("Сколько товаров хотите добавить? "))
shoppin_list = []
for i in range(goods_number):
    good = input("Введите товар: " ).strip() .lower() .replace("ё", "е")
    while good in shoppin_list:
        print("Такой товар уже есть в списке.")
        good = input("Введите товар: " ).strip() .lower() .replace("ё", "е")
    shoppin_list.append(good)
print(f"Ваш список: {shoppin_list}")
search_number = int(input("Сколько товаров хотите найти? "))
for i in range(search_number):
    good = input("Введите наименование товара: ").strip() .lower().replace("ё", "е")
    found = False
    for item in shoppin_list:
        if good in item:
            found = True
            print(f"Товар найден: {item}" )
    if found == False:
        print("Товар не найден")
while True:
    answer = input("Хотите удалить товар? Д/Н ").strip() .lower()
    if answer == "н":
        break
    if answer == "д":
        good = input("Какой товар хотите удалить? ").strip() .lower().replace("ё", "е")
        delete_choice = input("Удалить 1 товар или все? 1/2: ").strip()
        while delete_choice != "1" and delete_choice != "2":
            print("Неверная команда! Выберите 1 или 2")
            delete_choice = input("Удалить 1 товар или все? 1/2: ").strip()
        if delete_choice == "1":
            if good in shoppin_list:
                shoppin_list.remove(good)
                print(f"Обновленный список: {shoppin_list}")
            else:
                print("Данный товар отсутствует")
        elif delete_choice == "2":
            if good in shoppin_list:
                while good in shoppin_list:
                    shoppin_list.remove(good)
                print(f"Обновленный список: {shoppin_list}")
            else:
                print("Данный товар отсутствует")
else:
    print("Неверный ответ! Введите д или н ")
print(f"Итоговый список покупок: {shoppin_list}")