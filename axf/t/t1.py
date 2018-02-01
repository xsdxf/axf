import time
def count_time(fuc):
    def wrapper(c,d):
        begin=time.time()
        fuc(c,d)
        end=time.time()
        print(end-begin)
    return wrapper
@count_time
def fun1(a,b):
    sum=0
    for i in range(a,b):
        sum+=i
    print("fun1结果为",sum,"参数为",a,b)
fun1(10,10**8)