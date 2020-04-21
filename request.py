import requests
import json
from collections import OrderedDict

url = "https://api.codenation.dev/v1/challenge/dev-ps/generate-data?token=SEU_TOKEN"

# requisition result
r = requests.get(url).json(object_pairs_hook=OrderedDict)

with open('answer.json', 'w', encoding='utf-8') as file:
    json.dump(r, file, ensure_ascii=False, indent=2)