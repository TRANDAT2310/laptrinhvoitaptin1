import os
import numpy as np
def bai_5():
    list1 = np.random.randint(-1000,1000,size=1000)
    than = open("check.txt", mode="w", encoding="utf-8")
    x = 0
    for i in range(100):
        for J in range(0,10):
            than.write(f"{list1[x]}, ")
            x = x + 1
        than.write('\n')
    than = open('check.txt',mode="r")
    for sua in than.readline():
        print(replace(',',"\t"))
def main():
    datlam = bai_5()
if __name__=='__main__':
    main()