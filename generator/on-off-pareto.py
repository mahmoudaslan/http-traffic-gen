#!/usr/bin/env python
import numpy as np
import multiprocessing as mp
import time

def pareto(scale, shape):
    """
    Generates a pareto random variable.
    """
    return ((np.random.pareto(shape, 1) + 1) * scale)[0]

def req_times_gen(conf):
    req_lists = [[] for x in range(conf.clients_num)]
    #Pareto params, NS2 = true for default NS2 settings
    if conf.NS2:
        shape = 1.5
        mean_on = 0.5 #500ms
        mean_off = 0.5 #500ms
        burstlen = conf.reqs_rate * mean_on
        scale_on = burstlen * ((shape - 1)/shape)
        scale_off = mean_off * ((shape - 1)/shape)
        
    total_time = 0
    total_reqs = 0
    burst_num = 0
    while total_time < conf.gen_time:
        next_burstlen = int(pareto(scale_on, shape) + 0.5)
        burst_num += 1
        if not next_burstlen:
            next_burstlen = 1
        total_reqs += next_burstlen
        for i in range(next_burstlen):
            rnd_cli = int(np.random.uniform(0, conf.clients_num, size=1))
            req_lists[rnd_cli].append(total_time)
        next_idle_time = pareto(scale_off, shape)
        total_time += next_idle_time
        print "Next burst length:", next_burstlen, "Next idle time:", next_idle_time
    print "End time:", total_time, "Total num of reqs:", total_reqs
    return req_lists

def generate(conf, httpreq):
    req_lists = req_times_gen(conf)

    ps = []
    for i in range(conf.clients_num):
        p = mp.Process(target=send_req, args=(httpreq, req_lists[i]))
        ps.append(p)
        p.start()

def send_req(httpreq, req_list):
    resp = httpreq.send(req_list)
