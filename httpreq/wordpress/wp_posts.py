from wordpress_xmlrpc import Client, WordPressPost
from wordpress_xmlrpc.methods.posts import GetPosts, NewPost
from wordpress_xmlrpc.methods.users import GetUserInfo
from wordpress_xmlrpc.methods import media
from wordpress_xmlrpc.compat import xmlrpc_client
import requests
import numpy as np
import random
import time
import string

class WPPost(object):
    """ WPPost class is used for sending GET/POST requests to a wordpress website.
    
    Typical use:
    wp = WPPost(conf)

    """
    def __init__(self, conf):
        self.conf = conf
        self._connect()

    def _connect(self):
        self.wp_client = Client(self.conf.wp_hostxmlrpc,
                                self.conf.wp_user,
                                self.conf.wp_pass)

    #TODO: media directory should be defined in the conf file and a randomly chose media file should be picked
    def post(self):
        filename = "linuxlogo.jpg"
        data = {
            'name': 'linuxlogo.jpg',
            'type': 'image/jpeg',
        }
        with open(filename, 'rb') as img:
            data['bits'] = xmlrpc_client.Binary(img.read())

        r = self.wp_client.call(media.UploadFile(data))
        attachment_id = r['id']

        #Create random content in range of 1000 letters
        s = np.random.uniform(0, 1, size=2)
        s1 = int(s[0]*self.conf.post_nchars+1)
        s2 = int(s[1]*self.conf.post_title_nchars+1)
        
        content = "".join([random.choice(string.letters) for i in xrange(s1)])
        random_title = "".join([random.choice(string.letters) for i in xrange(s2)])
        
        post = WordPressPost()
        post.title = 'Random title: ' + random_title
        post.content = content
        post.post_status = 'publish'
        post.thumbnail = attachment_id
        post.terms_names = {
            'post_tag': ['test', 'firstpost'],
            'category': ['Uncategorized']
        }
        return self.wp_client.call(NewPost(post))

    #TODO: Should be random get
    def get(self):
        return requests.get(self.conf.wp_host)
