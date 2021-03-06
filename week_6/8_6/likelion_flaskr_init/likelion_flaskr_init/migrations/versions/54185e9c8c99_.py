"""empty message

Revision ID: 54185e9c8c99
Revises: 3262a3aa37b2
Create Date: 2014-08-06 19:55:26.214000

"""

# revision identifiers, used by Alembic.
revision = '54185e9c8c99'
down_revision = '3262a3aa37b2'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('article', sa.Column('author', sa.String(length=255), nullable=True))
    op.add_column('article', sa.Column('category', sa.String(length=255), nullable=True))
    op.add_column('article', sa.Column('date_created', sa.DateTime(), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('article', 'date_created')
    op.drop_column('article', 'category')
    op.drop_column('article', 'author')
    ### end Alembic commands ###
