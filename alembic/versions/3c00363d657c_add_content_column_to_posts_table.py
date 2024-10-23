"""add content column to posts table

Revision ID: 3c00363d657c
Revises: 0dd9f3d1ddc9
Create Date: 2024-10-23 16:02:24.839053

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '3c00363d657c'
down_revision: Union[str, None] = '0dd9f3d1ddc9'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts', 'content')
    pass
