from oslo_config import cfg
from oslo_db import api as db_api


_BACKEND_MAPPING = {'sqlalchemy': 'olsodb.db.sqlalchemy.api'}


IMPL = db_api.DBAPI.from_config(cfg.CONF, backend_mapping=_BACKEND_MAPPING)

def configure(conf):
    IMPL.configure(conf)


def get_context():
    return IMPL.get_context()


def create_foo(context, value):
    return IMPL.create_foo(context, value)
