"""migrazione iniziale

Revision ID: 830a8c279d5b
Revises: 
Create Date: 2024-06-04 23:02:55.991078

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '830a8c279d5b'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('appuntamenti', schema=None) as batch_op:
        batch_op.add_column(sa.Column('phone', sa.String(length=20), nullable=False))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('appuntamenti', schema=None) as batch_op:
        batch_op.drop_column('phone')

    # ### end Alembic commands ###