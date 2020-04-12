list = ['A = [1 2 ; 4 5]', 'B = [1 2 ; 4 5]']

f = open('test.txt', 'w')
f.write('\n'.join(list))

rf = open('test.txt', 'r')


for i in rf.readlines():
    print(i)