import os
import yaml


def singleton(cls):
    instances = {}

    def get_instances():
        if cls not in instances:
            instances[cls] = cls()
        return instances[cls]

    return get_instances


@singleton
class YamlRead:
    def __init__(self, file_path='config.yaml'):
        self.file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), file_path)
        with open(self.file_path, encoding='utf-8') as f:
            self.data = yaml.load(f, Loader=yaml.FullLoader)

    def get_data(self):
        return self.data


def get(key):
    data = YamlRead().get_data()
    return data.get('config').get(key, None)
