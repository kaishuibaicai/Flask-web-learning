"""add category model
Revision ID: 8f573a02d821
Revises: 1f6f103026a7
Create Date: 2016-07-20 19:50:29.225297
"""

# revision identifiers, used by Alembic.
revision = 'd372a1c0004f'
down_revision = 'a32de0710ec4'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('category',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('category', sa.Unicode(length=128), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('category')
    )
    op.add_column(u'posts', sa.Column('category_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'posts', 'category', ['category_id'], ['id'])
    ### end Alembic commands ###

def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'posts', type_='foreignkey')
    op.drop_column(u'posts', 'category_id')
    op.drop_table('category')
    ### end Alembic commands ###
