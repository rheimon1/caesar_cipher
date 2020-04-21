import requests
import json
from collections import OrderedDict

url = "https://api.codenation.dev/v1/challenge/dev-ps/generate-data?token=SEU_TOKEN"

# requisition result
r = requests.get(url).json(object_pairs_hook=OrderedDict)

# pretty print JSON String
data_formatted = json.dumps(r, indent=2, ensure_ascii=False)

with open('answer.json', 'w', encoding='utf-8') as file:
    file.write(data_formatted)