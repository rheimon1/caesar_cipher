import json
import hashlib
from collections import OrderedDict


def decode_text(encrypted_text, shift):
    characters = 'abcdefghijklmnopqrstuvwxyz'

    # string to store the decode text
    decrypted_text = ''

    # decodes each character of the encoded text
    for letter in encrypted_text:
        if letter in characters:
            # get number of the encoded character
            number = characters.find(letter)

            # character number in the alphabet
            number = number - shift

            if number >= len(characters):
                number = number - len(characters)
            elif number < 0:
                number = number + len(characters)

            decrypted_text += characters[number]
        else:
            decrypted_text += letter
    return decrypted_text


# open json file
try:
    with open('answer.json', 'r') as file:
        json_file = file.read()
except Exception as error:
    print(error)

json_data = json.loads(json_file, object_pairs_hook=OrderedDict)

encrypted_text = json_data["cifrado"].lower()
shift = json_data["numero_casas"]
encoding = file.encoding

decrypted_text = decode_text(encrypted_text, shift)
json_data["decifrado"] = decrypted_text

summary = hashlib.sha1(decrypted_text.encode(encoding)).hexdigest()
json_data['resumo_criptografico'] = summary

with open('answer.json', 'w') as file:
    json.dump(json_data, file, indent=2)


