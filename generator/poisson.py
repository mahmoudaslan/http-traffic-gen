#!/usr/bin/env python
import numpy as np
import multiprocessing as mp
import time

def poisson_interarrivals(conf):
    np.random.seed()
    total_reqs_per_client = int((conf.reqs_rate / conf.clients_num) * conf.gen_time)
    _lamda = float(conf._lamda/total_reqs_per_client)
    print _lamda, total_reqs_per_client
    return np.random.exponential(_lamda, total_reqs_per_client)

def req_times_gen(conf):
    """ This function generates a list of request times for each client. """
    total_reqs_per_client = int((conf.reqs_rate / conf.clients_num) * conf.gen_time)
    req_lists = [[] for x in range(conf.clients_num)]
    for j in range(conf.clients_num):
        s = poisson_interarrivals(conf) * total_reqs_per_client        
        for i in range(1, len(s)):
            s[i] += s[i-1]
        
        req_lists[j] = s
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
