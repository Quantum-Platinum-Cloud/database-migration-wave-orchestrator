# Copyright 2022 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""add restore_configs

Revision ID: fd984d3f7fe2
Revises: 32c827858686
Create Date: 2022-04-05 18:10:20.666220

"""
from alembic import op
import sqlalchemy as sa



# revision identifiers, used by Alembic.
revision = 'fd984d3f7fe2'
down_revision = '32c827858686'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('restore_configs',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('db_id', sa.Integer(), nullable=False),
    sa.Column('backup_location', sa.String(), nullable=True),
    sa.Column('rman_cmd', sa.Text(), nullable=True),
    sa.Column('is_configured', sa.Boolean(), nullable=True),
    sa.Column('pfile_file', sa.String(), nullable=True),
    sa.Column('pwd_file', sa.String(), nullable=True),
    sa.Column('tnsnames_file', sa.String(), nullable=True),
    sa.Column('listener_file', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['db_id'], ['source_dbs.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('db_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('restore_configs')
    # ### end Alembic commands ###
