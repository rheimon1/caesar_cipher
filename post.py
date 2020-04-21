import requests


def send_form():
    url = "https://api.codenation.dev/v1/challenge/dev-ps/submit-solution?token=SEU_TOKEN"
    answer = {'answer': open('answer.json', 'rb')}
    requests.post(url, files=answer)


send_form()

