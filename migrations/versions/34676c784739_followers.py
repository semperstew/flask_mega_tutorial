"""followers

Revision ID: 34676c784739
Revises: 5ceda8ba218a
Create Date: 2019-01-20 18:49:51.047246

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '34676c784739'
down_revision = '5ceda8ba218a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('followers',
    sa.Column('follower_id', sa.Integer(), nullable=True),
    sa.Column('followed_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['followed_id'], ['user.id'], ),
    sa.ForeignKeyConstraint(['follower_id'], ['user.id'], )
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('followers')
    # ### end Alembic commands ###
