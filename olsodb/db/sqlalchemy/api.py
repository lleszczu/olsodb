import sys

from oslo_db.sqlalchemy import enginefacade

from olsodb.db.sqlalchemy import models


storage_context_manager = enginefacade.transaction_context()


@enginefacade.transaction_context_provider
class Context(object):
    pass


def configure(conf):
    cfg = {'sqlite_fk': True, 'max_retries': 5}
    cfg.update(conf)
    storage_context_manager.configure(**cfg)


def get_backend():
    return sys.modules[__name__]


def get_context():
    return Context()


def create_foo(context, value):
    foo = models.Foo()
    foo.value = value
    context.session.add(foo)
    return foo
