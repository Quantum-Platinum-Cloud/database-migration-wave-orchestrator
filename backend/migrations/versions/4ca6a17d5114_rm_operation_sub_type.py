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

"""rm Operation.sub_type

Revision ID: 4ca6a17d5114
Revises: d8ce5cab768d
Create Date: 2022-06-01 15:07:39.085233

"""
from alembic import op
import sqlalchemy as sa



# revision identifiers, used by Alembic.
revision = '4ca6a17d5114'
down_revision = 'd8ce5cab768d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('operations', 'sub_type')
    op.alter_column('restore_configs', 'backup_type',
               existing_type=sa.VARCHAR(),
               nullable=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('restore_configs', 'backup_type',
               existing_type=sa.VARCHAR(),
               nullable=False)
    op.add_column('operations', sa.Column('sub_type', sa.VARCHAR(length=20), autoincrement=False, nullable=True))
    # ### end Alembic commands ###
