"""empty message

Revision ID: 5c587282a5c6
Revises: 310a0e7ec4d8
Create Date: 2023-08-11 23:45:31.141112

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5c587282a5c6'
down_revision = '310a0e7ec4d8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('charaters',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('type', sa.String(length=250), nullable=False),
    sa.Column('name', sa.String(length=250), nullable=False),
    sa.Column('birth_year', sa.String(length=250), nullable=False),
    sa.Column('eyes_color', sa.String(length=250), nullable=False),
    sa.Column('gender', sa.String(length=250), nullable=False),
    sa.Column('hair_color', sa.String(length=250), nullable=False),
    sa.Column('skin_color', sa.String(length=250), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('planets',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('type', sa.String(length=250), nullable=False),
    sa.Column('name', sa.String(length=250), nullable=False),
    sa.Column('terrain', sa.String(length=250), nullable=False),
    sa.Column('climate', sa.String(length=250), nullable=False),
    sa.Column('population', sa.String(length=250), nullable=False),
    sa.Column('orbital_period', sa.String(length=250), nullable=False),
    sa.Column('rotation_period', sa.String(length=250), nullable=False),
    sa.Column('diameter', sa.String(length=250), nullable=False),
    sa.Column('gravity', sa.String(length=250), nullable=False),
    sa.Column('surface_water', sa.String(length=250), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('favorites',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('item_type', sa.String(length=250), nullable=False),
    sa.Column('item_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('favorites')
    op.drop_table('planets')
    op.drop_table('charaters')
    # ### end Alembic commands ###
