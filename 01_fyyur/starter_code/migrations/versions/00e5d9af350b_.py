"""empty message

Revision ID: 00e5d9af350b
Revises: 56d47379904e
Create Date: 2022-08-20 06:49:04.265224

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '00e5d9af350b'
down_revision = '56d47379904e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('shows', sa.Column('artist_id', sa.Integer(), nullable=False))
    op.create_foreign_key(None, 'shows', 'Artists', ['artist_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'shows', type_='foreignkey')
    op.drop_column('shows', 'artist_id')
    # ### end Alembic commands ###
