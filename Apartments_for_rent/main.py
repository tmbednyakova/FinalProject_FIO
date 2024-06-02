from tkinter import *
from Apartments_for_rent.Apartment import Apartment


# Приложение обладает следующим функционалом:
# - посмотреть список квартир,
# - добавить информацию о квартире;
# - удалить квартиру из списка;
# - изменить статус квартиры (свободна/


def add_apartment():
    # для считывания данных их поля ввода
    # используется метод get()
    address = entry_address.get()
    square = entry_square.get()
    number_of_rooms = entry_number_of_rooms.get()
    rent_price = entry_rent_price.get()
    description = entry_description.get()
    # cоздается объект
    apartment = Apartment(address, square, number_of_rooms, rent_price, description)
    # добавить объект в список
    list_flat.append(apartment)
    # обновить Listbox
    list_flat_var.set(list_flat)


def delete():
    # получить индекс выбранного элемента
    index = apartments_listbox.curselection()
    # удалить элемент
    # remove удаляет по значению, а не по индексу
    # index[0] -  так как curselection()
    # возвращает список всех выбранных элементов
    # берем единственный, поэтому указываем индекс 0
    list_flat.remove(list_flat[index[0]])
    # и переопределяем ListBox
    list_flat_var.set(list_flat)


def rental():
    index = apartments_listbox.curselection()
    list_flat[index[0]].to_rent()
    list_flat_var.set(list_flat)


def cancel():
    index = apartments_listbox.curselection()
    list_flat[index[0]].cancel_rental()
    list_flat_var.set(list_flat)


if __name__ == '__main__':
    root = Tk()  # создаем корневой объект - окно
    root.title("аренда квартир")  # устанавливаем заголовок окна
    root.geometry("600x400")  # устанавливаем размеры окна

    label_address = Label(text="Введите адрес")  # создаем текстовую метку
    label_address.pack()  # размещаем метку в окне
    # поле ввода для адреса
    entry_address = Entry()  # создаем поле ввода
    entry_address.pack()  # размещаем поле ввода в окне

    label_square = Label(text="Площадь")  # создаем текстовую метку
    label_square.pack()  # размещаем метку в окне
    # поле ввода для площади
    entry_square = Entry()
    entry_square.pack()

    label_number_of_rooms = Label(text="Количество комнат")
    label_number_of_rooms.pack()
    entry_number_of_rooms = Entry()
    entry_number_of_rooms.pack()

    label_rent_price = Label(text="стоимость аренды за сутки")
    label_rent_price.pack()
    entry_rent_price = Entry()
    entry_rent_price.pack()

    label_description = Label(text="Описание")
    label_description.pack()
    entry_description = Entry()
    entry_description.pack()

    # кнопка для добавления квартиры
    btn_add_apartment = Button(text="Добавить квартиру", command=add_apartment)
    btn_add_apartment.pack()

    list_flat = []  # список для хранения квартир
    # создать объект "квартира"
    # apartment = Apartment("Дубна, Университетская, 19", 300, 5, 4000, "Отличный варинат для семьи. Рядом парк, больница, магазины, школы.")
    #  добавить объект в список
    # list_flat.append(apartment)
    # сохранить созданный и заполненный список в перменную типа Variable
    list_flat_var = Variable(value=list_flat)
    # создать ListBox, шириной 50 символов,
    # в котором будет отображаться список list_flat_var
    apartments_listbox = Listbox(width=50, listvariable=list_flat_var)
    # добавить ListBox на форму
    apartments_listbox.pack()

    btn_del_apartment = Button(text="Удалить", command=delete)
    btn_del_apartment.pack()

    btn_rent_apartment = Button(text="Сдать квартиру", command=rental)
    btn_rent_apartment.pack()

    btn_change_rent_apartment = Button(text="Освободить квартиру", command=cancel)
    btn_change_rent_apartment.pack()

    # строка ВСЕГДА должна быть последней!
    root.mainloop()
