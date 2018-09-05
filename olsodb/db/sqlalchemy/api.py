import sys
import alembic

import alembic.migration as alembic_migration

from oslo_db.sqlalchemy import enginefacade
from oslo_db.sqlalchemy import migration
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

@enginefacade.writer
def create_foo(context, value):
    foo = models.Foo()
    foo.value = value
    context.session.add(foo)
    return foo

def create_schema(config=None, engine=None):
    """Create database schema from models description.
    Can be used for initial installation instead of upgrade('head').
    """
    if engine is None:
        engine = enginefacade.writer.get_engine()

    # NOTE(viktors): If we will use metadata.create_all() for non empty db
    #                schema, it will only add the new tables, but leave
    #                existing as is. So we should avoid of this situation.
    if version(engine=engine) is not None:
        raise db_exc.DBMigrationError("DB schema is already under version"
                                      " control. Use upgrade() instead")

    models.DeclarativeBase.metadata.create_all(engine)


def version(config=None, engine=None):
    """Current database version.
    :returns: Database version
    :rtype: string
    """
    if engine is None:
        engine = enginefacade.writer.get_engine()
    with engine.connect() as conn:
        context = alembic_migration.MigrationContext.configure(conn)
        return context.get_current_revision()

