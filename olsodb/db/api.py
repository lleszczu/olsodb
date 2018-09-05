from oslo_config import cfg
from oslo_db import api as db_api
from oslo_db import options

_BACKEND_MAPPING = {'sqlalchemy': 'olsodb.db.sqlalchemy.api'}


IMPL = db_api.DBAPI.from_config(cfg.CONF, backend_mapping=_BACKEND_MAPPING)


def get_engine():
    return IMPL.get_engine()

def configure(conf):
    options.set_defaults(cfg.CONF)
    IMPL.configure(conf)


def get_context():
    return IMPL.get_context()


def create_foo(context, value):
    return IMPL.create_foo(context, value)

def create_schema():
    IMPL.create_schema()
