"""empty message

Revision ID: 4c83a2d87398
Revises: 5c587282a5c6
Create Date: 2023-08-11 23:48:52.849383

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4c83a2d87398'
down_revision = '5c587282a5c6'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('characters',
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
    op.drop_table('charaters')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('charaters',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('type', sa.VARCHAR(length=250), autoincrement=False, nullable=False),
    sa.Column('name', sa.VARCHAR(length=250), autoincrement=False, nullable=False),
    sa.Column('birth_year', sa.VARCHAR(length=250), autoincrement=False, nullable=False),
    sa.Column('eyes_color', sa.VARCHAR(length=250), autoincrement=False, nullable=False),
    sa.Column('gender', sa.VARCHAR(length=250), autoincrement=False, nullable=False),
    sa.Column('hair_color', sa.VARCHAR(length=250), autoincrement=False, nullable=False),
    sa.Column('skin_color', sa.VARCHAR(length=250), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name='charaters_pkey')
    )
    op.drop_table('characters')
    # ### end Alembic commands ###
