"""Add user status and FIO.

Revision ID: fc2ff13b2ecc
Revises: 0a6c4ced02cf
Create Date: 2024-09-18 21:53:04.289884

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'fc2ff13b2ecc'
down_revision: Union[str, None] = '0a6c4ced02cf'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('user', sa.Column('status', sa.Boolean(), default=True))
    op.add_column('user', sa.Column('FIO', sa.String(), default=''))



def downgrade() -> None:
    op.drop_column('user', 'status')
    op.drop_column('user', 'FIO')

