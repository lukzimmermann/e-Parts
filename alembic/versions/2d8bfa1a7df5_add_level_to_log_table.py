"""add level to log table

Revision ID: 2d8bfa1a7df5
Revises: a49a7f9f531f
Create Date: 2024-10-05 14:11:29.602779

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '2d8bfa1a7df5'
down_revision: Union[str, None] = 'a49a7f9f531f'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('log', sa.Column('level', sa.Integer(), nullable=False))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('log', 'level')
    # ### end Alembic commands ###
