"""empty message

Revision ID: 60925117ecf3
Revises: d463058c87a5
Create Date: 2022-08-19 16:27:52.448221

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '60925117ecf3'
down_revision = 'd463058c87a5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('genre')
    op.add_column('Artists', sa.Column('genres', sa.String(length=64), nullable=True))
    op.add_column('Venues', sa.Column('genres', sa.String(length=64), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('Venues', 'genres')
    op.drop_column('Artists', 'genres')
    op.create_table('genre',
    sa.Column('venues_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('artists_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('genre_name', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['artists_id'], ['Artists.id'], name='genre_artists_id_fkey'),
    sa.ForeignKeyConstraint(['venues_id'], ['Venues.id'], name='genre_venues_id_fkey'),
    sa.PrimaryKeyConstraint('venues_id', 'artists_id', name='genre_pkey')
    )
    # ### end Alembic commands ###