#1 task
immutable_var = 1, True, 'phone', [1,4,3]
print(immutable_var)

#2 task попытка изменить
# immutable_var[0] = 2 невозможно, так как кортеж является неизменяемой коллекцией.
# При попытке обратиться к элементу будет ошибка, которая дословно скажет что кортеж не
# поддерживает обращение по элементам. Но, кортеж может хранить изменяемые элементы, малую часть, например список
immutable_var[3][0] = 6
print(immutable_var)

#3 task
mutable_list = [1,'телефон',5,'стол',False]
print(mutable_list)
mutable_list.append('Reboot')
mutable_list.remove(False)
print(mutable_list)