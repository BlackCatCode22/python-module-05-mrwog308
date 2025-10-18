fclown = input('Enter filename: ')
if len(fclown) < 1 : fclown = 'clown.txt'
hand = open(fclown)

webster = {}

for line in hand:
    line = line.rstrip()

    words = line.split()

    for w in words:
        webster[w] = webster.get(w, 0) + 1

# print(webster)
big = -1
bigword = None
for k, v in webster.items():
    # print(k, v)
    if v > big:
        big = v
        bigword = k
print('The biggest value is:', bigword, big)