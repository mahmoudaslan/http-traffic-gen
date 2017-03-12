# http-traffic-gen
HTTP traffic generator

Currently, it supports poisson and on/off pareto. Configs can be changed in trafficgen.conf
Adding a new generator module is easy, just create the module file and change the trafficgen.confg file. The new module will be loaded dynamically.

Currently, the httpreq module is made for a wordpress server, its configs are in wordpress/wordpress.conf
Adding a new httpreq module is also easy since its loaded dynamically. Just create another folder inside httpreq and change the trafficgen.conf