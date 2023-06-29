sum_ch = 0 # сумма четных
num = 1 #номер числа по порядку (можно массивом,
# но я не помню как им сделать, та и думаю реализовал я проще))))
sum_on_ch = 0 # сумма числе стоящих на четных места
count = 0
for i in range(1, 100000):
    y = i
    x = i
    while i > 0:
        ch = i % 10
        i = i // 10
        if ch % 2 == 0:
            sum_ch += ch
        count += 1
    while count > 0:
        ch = x % 10
        x = x // 10
        if count % 2 == 0:
            sum_on_ch += ch
        count -= 1
    r = abs(sum_ch - sum_on_ch)
    if r == 22:
        print(y)
        break
    ch = 0
    sum_ch = 0
    sum_on_ch = 0




# i = 2021
# x = i
# while i > 0:
#     ch = i % 10
#     i = i // 10
#     if ch % 2 == 0:
#         sum_ch += ch
#     count += 1
# while count > 0:
#     ch = x % 10
#     x = x // 10
#     if count % 2 == 0:
#         sum_on_ch += ch
#     count -= 1
# r = abs(sum_ch - sum_on_ch)
# print(r)