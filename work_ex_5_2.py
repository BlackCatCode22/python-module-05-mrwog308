fclown = input('Enter filename: ')
if len(fclown) < 1 : fclown = 'clown.txt'
hand = open(fclown)

webster = {}

for line in hand:
    line = line.rstrip()
    words = line.split()

    for w in words:
        webster[w] = webster.get(w, 0) + 1

#find the top 5 words by frequency
# print(webster.items())
# print(sorted(webster.items()))
tmp = {}
newweb = []
for k, v in webster.items():
    tup = (v, k)
    newweb.append(tup)
    # print(tup)
# print(newweb)
# print(sorted(newweb, reverse=True)[:5])

cool = sorted(newweb, reverse=True)
# print(cool)

for v,k in cool[:5]:
    print(k, v)

# print(sorted([(v, k) for k, v in webster.items()], reverse=True)[:5])



