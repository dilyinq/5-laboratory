days_of_week = ('Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'Воскресенье')
num_weekends = int(input("Сколько выходных дней на неделе вы хотите? "))
weekends = days_of_week[-num_weekends:]
work_days = days_of_week[:-num_weekends]
print("Ваши выходные дни:", ", ".join(weekends))
print("Ваши рабочие дни:", ", ".join(work_days))
