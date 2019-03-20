from boyer_moore import boyer_moore, naive_impl
from z_algo import run_z
from KMP import kmp
import timeit
import time
import threading
from readfile import read_reference_file, pattern_generator

# class myThread (threading.Thread):
#     def __init__(self, threadID, algo_func, ppath, text):
#         threading.Thread.__init__(self)
#         self.threadID = threadID
#         self.algo_func = algo_func
#         self.ppath = ppath
#         self.text = text
#     def run(self):
#         print ("Starting " + self.name)
#         run_matching(self.algo_func, self.ppath, self.text)
#         print ("Exiting " + self.name)

def run_matching(algo, ppath, text):
    pgen = pattern_generator(ppath)
    start = timeit.default_timer()
    for pattern in pgen:
        algo(pattern, text)
        # break
    end = timeit.default_timer()
    t = end - start
    return time.strftime('%H:%M:%S', time.gmtime(t))

if __name__ == "__main__":
    ppath = 'pattern-collection.txt'
    text = read_reference_file()
    tz = run_matching(run_z, ppath,text)
    # tkmp = run_matching(kmp, ppath,text)
    tbm = run_matching(boyer_moore, ppath,text)
    print("time for z algo:", tz)
    # print("time for kmp:", tkmp)
    print("time for boyer moore:", tbm)



