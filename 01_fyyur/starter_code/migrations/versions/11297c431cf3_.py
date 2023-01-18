"""empty message

Revision ID: 11297c431cf3
Revises: 9720f45c857f
Create Date: 2022-08-20 09:28:26.697193

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '11297c431cf3'
down_revision = '9720f45c857f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('shows_artist_id_fkey', 'shows', type_='foreignkey')
    op.drop_column('shows', 'start_time')
    op.drop_column('shows', 'artist_id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('shows', sa.Column('artist_id', sa.INTEGER(), autoincrement=False, nullable=False))
    op.add_column('shows', sa.Column('start_time', postgresql.TIMESTAMP(), autoincrement=False, nullable=False))
    op.create_foreign_key('shows_artist_id_fkey', 'shows', 'Artists', ['artist_id'], ['id'])
    # ### end Alembic commands ###
