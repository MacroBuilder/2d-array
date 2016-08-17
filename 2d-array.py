import sys

'''
Provided by HackerRank '''
arr = []
for arr_i in range(6):
    arr_temp = map(int,input().strip().split(' '))
    arr.append(arr_temp)
''''''

hour = []
a = x = 0
b = y = 1

while x < 4:
    while a < 4:
        hour.append(sum([arr[x][j] for j in range(a, a+3)]) + arr[y][b] + sum([arr[x+2][j] for j in range(a, a+3)]))
        a += 1
        b += 1
    x += 1
    y += 1
    a = 0
    b = 1

print(max(hour))
