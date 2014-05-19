# Copyright 2014 Rackspace
# All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

from sqlalchemy import ForeignKey
from sqlalchemy.exc import OperationalError
from sqlalchemy.schema import Column
from sqlalchemy.schema import MetaData

from trove.db.sqlalchemy.migrate_repo.schema import create_tables
from trove.db.sqlalchemy.migrate_repo.schema import drop_tables
from trove.db.sqlalchemy.migrate_repo.schema import String
from trove.db.sqlalchemy.migrate_repo.schema import Table
from trove.openstack.common import log as logging

logger = logging.getLogger('trove.db.sqlalchemy.migrate_repo.schema')

meta = MetaData()

ds_versions_members = Table(
    'datastore_versions_members',
    meta,
    Column('id', String(36), primary_key=True, nullable=False),
    Column('datastore_version_id', String(36), nullable=False, ForeignKey("datastore_versions.id"),
    Column('tenant_id', String(36), nullable=False),
    Column('craeted_at', DateTime()),
)


def upgrade(migrate_engine):
    meta.bind = migrate_engine
    try:
        create_tables([ds_versions_members])
    except OperationalError as e:
        logger.info(e)


def downgrade(migrate_engine):
    meta.bind = migrate_engine
    drop_tables([datastore_versions_members])
