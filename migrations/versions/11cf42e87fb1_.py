"""empty message

Revision ID: 11cf42e87fb1
Revises: 81ff558ee0f9
Create Date: 2023-08-18 14:33:56.964444

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '11cf42e87fb1'
down_revision = '81ff558ee0f9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('characters', schema=None) as batch_op:
        batch_op.drop_column('type')

    with op.batch_alter_table('planets', schema=None) as batch_op:
        batch_op.drop_column('type')

    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.alter_column('is_active',
               existing_type=sa.BOOLEAN(),
               nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.alter_column('is_active',
               existing_type=sa.BOOLEAN(),
               nullable=False)

    with op.batch_alter_table('planets', schema=None) as batch_op:
        batch_op.add_column(sa.Column('type', sa.VARCHAR(length=250), autoincrement=False, nullable=True))

    with op.batch_alter_table('characters', schema=None) as batch_op:
        batch_op.add_column(sa.Column('type', sa.VARCHAR(length=250), autoincrement=False, nullable=True))

    # ### end Alembic commands ###
