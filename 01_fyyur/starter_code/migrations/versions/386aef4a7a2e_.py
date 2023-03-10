"""empty message

Revision ID: 386aef4a7a2e
Revises: bf70a12953c6
Create Date: 2022-08-20 09:57:08.343242

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '386aef4a7a2e'
down_revision = 'bf70a12953c6'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('shows', sa.Column('artist_id', sa.Integer(), nullable=True))
    op.add_column('shows', sa.Column('start_time', sa.DateTime(), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('shows', 'start_time')
    op.drop_column('shows', 'artist_id')
    # ### end Alembic commands ###
