import os
def bai_3():
    huy = ["yeu than"]
    than = open("check.txt", mode="w", encoding="utf-8")
    than.writelines(huy)
    than.close()
def main():
    datlam = bai_3()
if __name__=='__main__':
    main()