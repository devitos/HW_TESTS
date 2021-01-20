import requests


class YandexUser:
    def __init__(self, token: str):
        self.token = token

    def create_dir(self, dir_name: str):
        HEADERS = {'Authorization': f'OAuth {self.token}'}
        reponse = requests.put('https://cloud-api.yandex.net/v1/disk/resources',
                               params={'path': f'/{dir_name}', 'overwrite': True}, headers=HEADERS, )
        return reponse.status_code


if __name__ == '__main__':

    user1 = YandexUser('')          # Вставьте токен
    user1.create_dir('Testing_dir')
