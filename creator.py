import json, requests

class Creator:
    """ Class for Data Creation """

    def read_file(self, entity_type):
        """ read the file """
        with open('res/' + entity_type + '.json') as json_file:
            data = json.load(json_file)
            return data


    def create_entities(self, entity_type):
        """ read the file and create entities """
        data = self.read_file(entity_type)
        base_url = data['url']
        for entity in data['entities']:
            url = base_url + entity['url']
            for data in entity['entities']:
                r = requests.post(url, json.dumps(data))
                print(r.text)
