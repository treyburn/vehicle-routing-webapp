def load_key(path: str) -> str:
    """ Loads api key from secrets file."""

    with open(path) as fh:
        key = fh.read()
        return key


def _main():
    key_p = r'C:\Users\Travis\projects\vehicle-routing-webapp\unimplemented_code\secret.txt'
    key = load_key(key_p)
    print(key)


if __name__ == '__main__':
    _main()
