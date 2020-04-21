import requests
import json
import hashlib
from collections import OrderedDict

def save_content_json(response):
    # format dictionary
    data_formatted = json.dumps(response, indent=2)

    with open('answer.json', 'w') as file:
        file.write(data_formatted)


def open_content_json():
    try:
        json_file = open('answer.json', 'r+')
        return json_file
    except Exception as error:
        return error


def decode_text(cifrado, numero_casas):
    characters = 'abcdefghijklmnopqrstuvwxyz'

    # string to store the decode text
    decifrado = ''

    # decodes each character of the encoded text
    for letter in cifrado:
        if letter in characters:
            # get number of the encoded character
            aux = characters.find(letter)

            # character number in the alphabet
            aux = aux - numero_casas

            if aux >= len(characters):
                aux = aux - len(characters)
            elif aux < 0:
                aux = aux + len(characters)

            decifrado += characters[aux]
        else:
            decifrado += letter
    return decifrado

# requisition result
response = requests.get("https://api.codenation.dev/v1/challenge/dev-ps/generate-data?token=")

# convert bytes to dictionary
response = json.loads(response.content.decode('utf-8'), object_pairs_hook=OrderedDict)

# content requisition
save_content_json(response)

# open json file
json_file = open_content_json()
json_data = json.load(json_file, object_pairs_hook=OrderedDict)

cifrado = json_data["cifrado"].lower()
numero_casas = json_data["numero_casas"]

decifrado = decode_text(cifrado, numero_casas)

json_data['decifrado'] = decifrado

save_content_json(json_data)


json_file = open_content_json()

encoding = json_file.encoding

resumo = hashlib.sha1(decifrado.encode(encoding)).hexdigest()
json_data['resumo_criptografico'] = resumo

save_content_json(json_data)