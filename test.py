import sys

from olsodb.db import api
from oslo_config import cfg


def main():
    cfg.CONF(sys.argv[1:],
            project='olsodb')
    api.configure({})
    api.create_schema()
    ctx = api.get_context()

    api.create_foo(ctx, 'jakies gowno')


if __name__ == "__main__":
    main()
