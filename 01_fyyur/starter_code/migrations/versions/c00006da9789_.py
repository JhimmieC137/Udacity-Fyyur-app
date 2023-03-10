"""empty message

Revision ID: c00006da9789
Revises: b218d7d0dab4
Create Date: 2022-08-19 22:41:47.290530

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c00006da9789'
down_revision = 'b218d7d0dab4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('genre')
    op.add_column('Venues', sa.Column('genres', sa.ARRAY(sa.String(length=120)), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('Venues', 'genres')
    op.create_table('genre',
    sa.Column('venues_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('artists_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('genre_name', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['artists_id'], ['Artists.id'], name='genre_artists_id_fkey'),
    sa.ForeignKeyConstraint(['venues_id'], ['Venues.id'], name='genre_venues_id_fkey'),
    sa.PrimaryKeyConstraint('venues_id', 'artists_id', name='genre_pkey')
    )
    # ### end Alembic commands ###
