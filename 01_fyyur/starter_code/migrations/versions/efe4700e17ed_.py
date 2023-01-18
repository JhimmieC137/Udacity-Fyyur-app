"""empty message

Revision ID: efe4700e17ed
Revises: 034f5adb3eef
Create Date: 2022-08-19 14:35:36.710882

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'efe4700e17ed'
down_revision = '034f5adb3eef'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Artists', sa.Column('genres', sa.String(length=64), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('Artists', 'genres')
    # ### end Alembic commands ###