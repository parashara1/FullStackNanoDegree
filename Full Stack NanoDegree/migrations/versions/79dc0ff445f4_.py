"""empty message

Revision ID: 79dc0ff445f4
Revises: 
Create Date: 2020-10-10 18:22:22.306828

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '79dc0ff445f4'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('todos',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('description', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('todos')
    # ### end Alembic commands ###
