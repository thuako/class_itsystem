import sys
test_flag = 1

if test_flag == 1:
    f1 = open("c:\\python\\test1.txt", 'r')

    a = f1.readlines()

    print(len(a[0]), len(a[1]))

if test_flag ==2:
    if len(sys.argv) < 6:

        rt1 = open(sys.argv[1], 'r')
        a = rt1.readlines()

        if a[0] == a[1]:
            print("equal")
        else:
            print("different")
    else:
        print("error")

if test_flag ==3:
    class Hello:
        __num = 10  # private
        def __init__(self, number):
            self.num = number

        def inc(self):
            self.num = self.num +1
        def pri(self):
            print(self.num)
        def number(self):
            return self.num
    class Hello2(Hello):
        def __init__(self, number):
            super().__init__(number)
        def inc2(self):
            self.num = self.num +2

    a = Hello2(100)
    a.pri()
    a.inc()
    a.pri()
    a.inc()
    a.pri()
    a.inc2()
    a.pri()



if test_flag == 5:
    class myclass:
        __num = 10
        def __init__(self, number):
            self.__num = number
        def pri(self):
            print(self.__num)
        def ret(self):
            return self.__nu
    test = myclass(4)

    test.pri()



# f.read()  파일 전체를 읽음
# f.readline() 한라인씩 읽음
# f.readlines() 파일 전체를 받아서 리스트를 넘겨줌


if test_flag == 'hw':
    import os

    if len(sys.argv) == 1:
        os.system('python')
    else:
        f = open(sys.argv[1], 'r')

if test_flag == 'test':
    import