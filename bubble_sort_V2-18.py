#Команда из 9 дайверов направляется на исследование 3х затопленных кораблей в Тихом Океане.
#Перед отправкой оказалось, что все снаряжение было перепутано главным по складу и разложено не по номерам.
#К счастью каждый дайвер успел пронумеровать свое снаряжение.
#Задание номер 1: с помощью пузырьковой сортировки отсортировать  список снаряжения в порядке возрастания и вывести на экран первые 9 комплектов снаряжения.
#Задание номер 2: разбить дайверов на 3 группы и вывести на экран их состав, группа 1 (снаряжение номер 1,3,5), группа 2 (снаряжение номер 2,4,6), группа 3 (снаряжение 7,8,9)


N = 15
a = [2, 7, 3, 6, 78, 34, 67, 33, 8, 10, 52, 99, 44, 15, 20]
def bubble_sort(a):
    for i in range(N-1):
        for j in range(N-i-1):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
    return a


bubble_sort(a)

team_1 = (a[0], a[2], a[4])
team_2 = (a[1], a[3], a[5])
team_3 = (a[6], a[7], a[8])

print(a[0:9])

print(team_1, team_2, team_3)
