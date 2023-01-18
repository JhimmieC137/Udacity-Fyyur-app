"""empty message

Revision ID: 02f7194193b8
Revises: 8ad8df5c21f1
Create Date: 2022-08-19 15:46:25.531629

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '02f7194193b8'
down_revision = '8ad8df5c21f1'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('genre',
    sa.Column('venues_id', sa.Integer(), nullable=False),
    sa.Column('artists_id', sa.Integer(), nullable=False),
    sa.Column('genre name', sa.String(), nullable=False),
    sa.ForeignKeyConstraint(['artists_id'], ['Artists.id'], ),
    sa.ForeignKeyConstraint(['venues_id'], ['Venues.id'], ),
    sa.PrimaryKeyConstraint('venues_id', 'artists_id')
    )
    op.drop_table('genres')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('genres',
    sa.Column('venues_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('artists_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('genre name', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['artists_id'], ['Artists.id'], name='genres_artists_id_fkey'),
    sa.ForeignKeyConstraint(['venues_id'], ['Venues.id'], name='genres_venues_id_fkey'),
    sa.PrimaryKeyConstraint('venues_id', 'artists_id', name='genres_pkey')
    )
    op.drop_table('genre')
    # ### end Alembic commands ###
