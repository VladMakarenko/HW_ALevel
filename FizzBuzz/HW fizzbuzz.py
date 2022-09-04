def fizzbuzz(fizz, buzz, num):
    res_fb = []

    for i in range(1, num + 1):
        if not i % fizz and not i % buzz:
            res_fb.append('FB')
        elif not i % fizz:
            res_fb.append('F')
        elif not i % buzz:
            res_fb.append('B')
        else:
            res_fb.append(str(i))
    return ' '.join(res_fb)


file = open('fizzbuzznumbers.txt')
file_res = open('fizzbuzznumbers2.txt', 'w')

for line in file:
    fizz, buzz, num = map(int, line.split())
    print(line, '-->', fizzbuzz(fizz, buzz, num))
    file_res.write(fizzbuzz(fizz, buzz, num) + '\n')

file.close()
file_res.close()
