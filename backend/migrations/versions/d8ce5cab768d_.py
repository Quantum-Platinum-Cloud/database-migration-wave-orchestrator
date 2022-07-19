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

"""empty message

Revision ID: d8ce5cab768d
Revises: 32b82c34703c
Create Date: 2022-05-26 15:48:06.804205

"""
from alembic import op
import sqlalchemy as sa



# revision identifiers, used by Alembic.
revision = 'd8ce5cab768d'
down_revision = '32b82c34703c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('waves', 'description')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('waves', sa.Column('description', sa.VARCHAR(), autoincrement=False, nullable=False))
    # ### end Alembic commands ###