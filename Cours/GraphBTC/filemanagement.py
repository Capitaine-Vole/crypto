from configparser import ConfigParser

def writeFile(filename, content):
    with open(filename, "a+") as file:
        file.write(content + "\n")
        file.close

def createFile(filename):
    with open(filename, "w+") as file:
        file.close()

def readFile(filename):
    with open(filename, 'r+') as file:
        read = file.read()
        file.close()
        return read

# config

def getFromConfig(key, category='config', configfile='config.cfg'):
    config = ConfigParser()
    config.read(configfile)
    keyReturn = config[category][key]
    return keyReturn