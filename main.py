num = 30
fibonacci = []


def sumOfNumberBefore(list):
    return list[-2] + list[-1]


for i in range(num+1):
    if i <= 1:
        fibonacci.append(i)
        i += 1
    elif i >= 1:
        fibonacci.append(sumOfNumberBefore(fibonacci))
        i += 1

print(fibonacci)
