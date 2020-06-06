from requests import Response

from net_api import get_user, get_friends


def main():
    response = get_user('faceless_lord')['response'][0]
    user_id = response['id']

    friends = get_friends(user_id)['response']['items']
    fr_list = list(map(get_name, friends))

    print('\n'.join(fr_list))


def get_name(response: dict):
    return f'{response["first_name"]} {response["last_name"]}'


if __name__ == '__main__':
    main()
