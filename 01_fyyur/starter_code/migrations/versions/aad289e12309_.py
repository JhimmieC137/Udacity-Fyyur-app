"""empty message

Revision ID: aad289e12309
Revises: 6ffed2abfc25
Create Date: 2022-08-20 09:47:00.634462

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'aad289e12309'
down_revision = '6ffed2abfc25'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('shows', 'artist_id')
    op.drop_column('shows', 'start_time')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('shows', sa.Column('start_time', postgresql.TIMESTAMP(), autoincrement=False, nullable=False))
    op.add_column('shows', sa.Column('artist_id', sa.INTEGER(), autoincrement=False, nullable=True))
    # ### end Alembic commands ###
