import requests
import numpy as np
import random
import time
import string
import matplotlib
import matplotlib.pyplot as plt

def weibull():
    n_reqs = 3600
    a = 1.5
    s = np.random.weibull(a, n_reqs)
    print s
    arrival_arr = [0 for x in range(62)]
    arrival = 0
    num = 0
    start = time.time()
    for a in s:
        num += a
        arrival += a
        print arrival
        arrival_arr[int(arrival/60.0)] += 1

    print num
    fig = plt.figure(1)
    fig = fig.add_subplot(111)
    fig.set_xlabel("Time(mins)", fontsize=25)
    fig.set_ylabel("Number of requests", fontsize=25)
    fig.set_xticks([x*2 for x in range(62)])
    #fig.scatter([x for x in range(4000)], arrival_arr, c='b', marker='o')
    fig.plot([x for x in range(62)], arrival_arr, ls='-', c='b')
    plt.grid()
    plt.pause(60)


def generate():
    n_reqs = 3600 #Number of requests/hour for each client
    _lambda = 1.0/n_reqs
    s = np.random.exponential(_lambda, n_reqs)
    print s
    arrival_arr = [0 for x in range(61)]
    arrival = 0
    num = 0
    start = time.time()
    for a in s:
        num += 1
        arrival += a * n_reqs
        arrival_arr[int(arrival/60.0)] += 1
        #print '#',  num, arrival, a*n_reqs
    #print arrival_arr
    #print sum(arrival_arr)

    fig = plt.figure(1)
    fig = fig.add_subplot(111)
    fig.set_xlabel("Time(mins)", fontsize=25)
    fig.set_ylabel("Number of requests", fontsize=25)
    fig.set_xticks([x*2 for x in range(61)])
    #fig.scatter([x for x in range(4000)], arrival_arr, c='b', marker='o')
    fig.plot([x for x in range(61)], arrival_arr, ls='-', c='b')
    plt.grid()
    plt.pause(60)

if __name__ == '__main__':
    np.random.seed(5)
    #generate()
    weibull()
    
    
   
 
