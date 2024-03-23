group1 = ["Иванов", "Лебедева", "Ильин", "Смирнова", "Петров"]
group2 = ["Соколов", "Крючков", "Волочков", "Максимов", "Фетисова"]

team = tuple(group1 + group2)

print("Группа 1:", group1)
print("Группа 2:", group2)
print("Спортивная команда:", team)

print("Длина кортежа:", len(team))

sorted_team = sorted(team)
print("Отсортированная команда:", sorted_team)

ivanov_count = sorted_team.count('Иванов')
if ivanov_count > 0:
    print("Фамилия 'Иванов' встречается", ivanov_count, "раз в кортеже.")
else:
    print("Студент Иванов не входит в команду")
