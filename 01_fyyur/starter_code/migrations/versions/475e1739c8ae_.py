"""empty message

Revision ID: 475e1739c8ae
Revises: 60925117ecf3
Create Date: 2022-08-19 20:45:10.392697

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '475e1739c8ae'
down_revision = '60925117ecf3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('Artists', 'past_shows_count',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.alter_column('Artists', 'upcoming_shows_count',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.alter_column('Venues', 'past_shows_count',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.alter_column('Venues', 'upcoming_shows_count',
               existing_type=sa.INTEGER(),
               nullable=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('Venues', 'upcoming_shows_count',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.alter_column('Venues', 'past_shows_count',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.alter_column('Artists', 'upcoming_shows_count',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.alter_column('Artists', 'past_shows_count',
               existing_type=sa.INTEGER(),
               nullable=False)
    # ### end Alembic commands ###
