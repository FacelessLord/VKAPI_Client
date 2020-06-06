import sys

from net_api import get_user, get_friends


def main(uid, limit: int = -1):
    response = get_user(uid)['response'][0]
    user_id = response['id']

    friends_resp = get_friends(user_id, limit)
    friends = friends_resp['response']['items']
    fr_list = list(map(get_name, friends))

    if len(fr_list) == 0:
        print(f"User(id={uid}) doesn't have any friends")
    else:
        print('\n'.join(fr_list))


def get_name(response: dict):
    return f'{response["first_name"]} {response["last_name"]}'


def print_help():
    print('VKAPI Client')
    print('python runner.py ([OPTIONS] [ARGS])*')
    print()
    print('Options:')
    print('-f [user_id]: prints list of friends of user with id "user_id"')
    print('-l [max_count]: limits line count to "max_count"')


if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == '-f':
        if len(sys.argv) > 2:
            uid = sys.argv[2]
            if len(sys.argv) > 3 and sys.argv[3] == '-l':
                uid = sys.argv[2]
                if len(sys.argv) > 4:
                    lim = int(sys.argv[4])
                    main(uid, lim)
                else:
                    print('Need to specify count limit')
            else:
                main(uid)
        else:
            print('Need to specify user_id')
    else:
        print_help()
