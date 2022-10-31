
import yaml

def getConfig():
    with open("YamlConfig/config.yaml", encoding='utf8') as r:
        data = yaml.load(r, Loader=yaml.FullLoader)
        return data

def start():
    print("hankangwen")
    config = getConfig()
    sql = config['SQL']
    server = config['Server']
    print(sql['host'])
    print(server['host'])
