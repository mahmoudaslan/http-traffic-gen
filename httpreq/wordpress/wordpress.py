import requests
import os
import sys
import numpy as np
import random
import time
import string
import multiprocessing as mp
from wordpress_xmlrpc import Client, WordPressPost
from wordpress_xmlrpc.methods.posts import GetPosts, NewPost
from wordpress_xmlrpc.methods.users import GetUserInfo
from wordpress_xmlrpc.methods import media
from wordpress_xmlrpc.compat import xmlrpc_client
from conf import CONF
import wp_posts

wp_conf = None
try:
    wp_conf = CONF(r'httpreq/wordpress/wordpress.conf')
except Exception as e:
    print e
    sys.exit(1)
            

#Choose random requests(GET or POST) based on the given GET:POST ratio
def _choose_req():
    s = np.random.uniform(0, 1, size=1)
    if s <= wp_conf.post_ratio:
        return "POST"
    elif s <= wp_conf.post_ratio + wp_conf.get_ratio:
        return "GET"
                    
def send(req_list):
    try:
        wp = wp_posts.WPPost(wp_conf)
    except Exception as e:
        raise
        #print "Error connecting to wordpress host", e

    prev_req_time = 0
    for req_time in req_list:
        time.sleep(req_time - prev_req_time)
        prev_req_time = req_time
        req_type = _choose_req()
        try:
            resp = None
            if req_type == "POST":
                print "Time:", req_time, "PID:", os.getpid(), req_type + "Resp: " + str(wp.post())
            else:
                print "Time:", req_time, "PID:", os.getpid(), req_type + "Resp: " + str(wp.get())
        except Exception as e:
            print "Time:", req_time, "PID:", os.getpid(), req_type, "ERROR sending request!", e
