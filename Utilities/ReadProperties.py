import configparser

config = configparser.RawConfigParser()
config.read(".\\Congifurations\\config.ini")

class ReadConfig:

    @staticmethod
    def getApplicationURL():
        url = config.get('common info', 'applicationURL')
        return url

    # @staticmethod
    # def getUserName():
    #     url = config.get('common info', 'username')
    #     return url
    #
    # @staticmethod
    # def getUserEmail():
    #     username = config.get('common info', 'useremail')
    #     return username
    #
    # @staticmethod
    # def getUserPassword():
    #     password = config.get('common info', 'userpassword')
    #     return password
    #
    # @staticmethod
    # def getUserMobileNumber():
    #     url = config.get('common info', 'usermobilenumber')
    #     return url
    #



