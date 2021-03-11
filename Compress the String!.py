#Given integer as an example 5553322, and the output will (3, 5) (2, 3) (2, 2). It count how many the number shows.

S = int(input())

S = [int(x) for x in str(S)] 

poin = 0
i = S[0]

for j in range(len(S)):
    if i==S[j]:
        poin += 1
        if j == len(S)-1:
            print('(%d, %d)'%(poin,i))
    else:
        print('(%d, %d) '%(poin,i), end='')
        i=S[j]
        poin = 1
