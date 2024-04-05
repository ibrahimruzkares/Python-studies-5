import threading
import time

x = 8192

lock = threading.Lock()
def double():
    global x,lock
    lock.acquire()
    while x < 163842:
        x *= 2
        print(x)
        time.sleep(1)
    print("Reached the maximum.")
    lock.release()

def half():
    global x, lock
    lock.acquire()
    while x > 1:
        x /= 2
        print(x)
        time.sleep(1)
    print("Reached the minimum!")
    lock.release()

t1 = threading.Thread(target = double)
t2 = threading.Thread(target = half)

t1.start()
t2.start()

