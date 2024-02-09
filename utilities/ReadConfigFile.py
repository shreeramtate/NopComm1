
import configparser

configfile=configparser.RawConfigParser()
configfile.read("G:\\BALASAHEB\\CT16\\PRACTICE AUTOMATION\\NopCommerceLogin2\\Configuration\\config.ini")
# config.read("..\\Configuration\\config.ini")

class Readconfig:

    @staticmethod
    def getEmail():
        Email1=configfile.get('login data', 'email')
        return Email1

    @staticmethod
    def getPassword():
        Password1 = configfile.get('login data', 'password')
        return Password1


