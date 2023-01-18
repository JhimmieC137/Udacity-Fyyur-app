"""empty message

Revision ID: 67960f965c64
Revises: d58bcad241db
Create Date: 2022-08-16 10:37:38.230462

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '67960f965c64'
down_revision = 'd58bcad241db'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Artists', sa.Column('past_shows', sa.String(), nullable=True))
    op.add_column('Artists', sa.Column('upcoming_shows', sa.String(), nullable=True))
    op.add_column('Artists', sa.Column('past_shows_count', sa.Integer(), nullable=False))
    op.add_column('Artists', sa.Column('upcoming_shows_count', sa.Integer(), nullable=False))
    op.add_column('Venues', sa.Column('past_shows', sa.String(), nullable=True))
    op.add_column('Venues', sa.Column('upcoming_shows', sa.String(), nullable=True))
    op.add_column('Venues', sa.Column('past_shows_count', sa.Integer(), nullable=False))
    op.add_column('Venues', sa.Column('upcoming_shows_count', sa.Integer(), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('Venues', 'upcoming_shows_count')
    op.drop_column('Venues', 'past_shows_count')
    op.drop_column('Venues', 'upcoming_shows')
    op.drop_column('Venues', 'past_shows')
    op.drop_column('Artists', 'upcoming_shows_count')
    op.drop_column('Artists', 'past_shows_count')
    op.drop_column('Artists', 'upcoming_shows')
    op.drop_column('Artists', 'past_shows')
    # ### end Alembic commands ###
