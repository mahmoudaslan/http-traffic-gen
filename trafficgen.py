from conf import CONF
import importlib
import sys

if __name__ == "__main__":
    conf = None
    try:
        conf = CONF(r'trafficgen.conf')
    except Exception as e:
        print e
        sys.exit(1)

    #Import the traffic generator
    #This module should implement generate function that takes the httpserver object as an argument
    try:
        generator = importlib.import_module(conf.generator)
    except ImportError as e:
        print e
        sys.exit(1)


    #Import the httpserver module
    #This module should implement `send` request function
    try:
        httpreq = importlib.import_module(conf.httpreq)
        #if conf.httpmodule == "wordpress":
            #from wordpressreq import WPReq as httpreq
    except ImportError as e:
        print e
        sys.exit(1)
        
    generator.generate(conf, httpreq)
