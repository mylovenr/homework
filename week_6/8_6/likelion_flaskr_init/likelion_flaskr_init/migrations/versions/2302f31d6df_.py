"""empty message

Revision ID: 2302f31d6df
Revises: 2465ff675871
Create Date: 2014-08-12 16:55:39.673000

"""

# revision identifiers, used by Alembic.
revision = '2302f31d6df'
down_revision = '2465ff675871'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('comment', sa.Column('like', sa.Integer(), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('comment', 'like')
    ### end Alembic commands ###