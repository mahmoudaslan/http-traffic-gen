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
            self.wp_host = configParser.get('Wordpress', 'host')
            self.wp_hostxmlrpc = configParser.get('Wordpress', 'hostxmlrpc')
            self.wp_user = configParser.get('Wordpress', 'user')
            self.wp_pass = configParser.get('Wordpress', 'pass')

            self.get_ratio = configParser.getfloat('Posts', 'get_ratio')
            self.post_ratio = configParser.getfloat('Posts', 'post_ratio')
            self.media_path = configParser.get('Posts', 'media_path')
            self.post_nchars = configParser.getint('Posts', 'post_nchars')
            self.post_title_nchars = configParser.getint('Posts', 'post_title_nchars')
            
        except (ConfigParser.NoSectionError, ConfigParser.NoOptionError) as e:
            raise ValueError("Configuration parsing error: " + str(e))
            
