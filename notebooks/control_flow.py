
temps = [21.5, 23.0, 19.8]

for t in temps:
    if t > 24:
        print(t, "hot")
    elif t > 20:
        print(t, "warm")
    else:
        print(t, "cool")

i = 0
while i < 3:
    print(i)
    i += 1

def average(values):
    return sum(values) / len(values)

print(average(temps))
print(average([]))    # predict: ZeroDivisionError