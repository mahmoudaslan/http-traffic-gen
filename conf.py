import ConfigParser

class CONF(object):
    """ CONF class is used to parse the configuration file.

    Typical use:
    try:
        conf = CONF(file)
    except Exception as e:
        print e
        sys.exit(1)

    """
    def __init__(self, configFile):
        try:
            self._get_config(configFile)
        except:
            raise

    def _get_config(self, configFile):
        configParser = ConfigParser.RawConfigParser()
        if configParser.read(configFile) == []:
            raise ValueError("Configuration file not found: " + configFile)

        try:
            self.reqs_rate = configParser.getfloat('Default', 'reqs_rate')
            self.gen_time = configParser.getint('Default', 'gen_time')
            self.generator = configParser.get('Default', 'generator')
            self.httpreq = configParser.get('Default', 'httpreq')
            self.clients_num = configParser.getint('Default', 'clients_num')

            self._lamda = configParser.getfloat('Poisson', 'lamda')

            self.NS2 = configParser.getboolean('ON-OFF-Pareto', 'NS2')

            self.shape = configParser.getfloat('ON-OFF-Pareto', 'shape')
            self.mean_on = configParser.getfloat('ON-OFF-Pareto', 'mean_on')
            self.mean_off = configParser.getfloat('ON-OFF-Pareto', 'mean_off')
            self.burstlen = configParser.getfloat('ON-OFF-Pareto', 'burstlen')
            self.scale_on = configParser.getfloat('ON-OFF-Pareto', 'scale_on')
            self.scale_off = configParser.getfloat('ON-OFF-Pareto', 'scale_off')
            
        except (ConfigParser.NoSectionError, ConfigParser.NoOptionError) as e:
            raise ValueError("Configuration parsing error: " + str(e))
            
