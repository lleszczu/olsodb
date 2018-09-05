from olsodb.db import api


def main():
    api.configure({'connection': 'sqlite:////tmp/baza.sqlite'})
    ctx = api.get_context()

    api.create_foo(ctx, 'jakies gowno')


if __name__ == "__main__":
    main()
