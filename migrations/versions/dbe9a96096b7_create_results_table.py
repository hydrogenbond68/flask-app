"""create results table

Revision ID: dbe9a96096b7
Revises: aafbb3aff90c
Create Date: 2024-06-27 09:21:27.103017

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'dbe9a96096b7'
down_revision = 'aafbb3aff90c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('results',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('marks', sa.Integer(), nullable=False),
    sa.Column('student_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['student_id'], ['students.id'], name=op.f('fk_results_student_id_students')),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_results'))
    )
    with op.batch_alter_table('students', schema=None) as batch_op:
        batch_op.create_unique_constraint(batch_op.f('uq_students_email'), ['email'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('students', schema=None) as batch_op:
        batch_op.drop_constraint(batch_op.f('uq_students_email'), type_='unique')

    op.drop_table('results')
    # ### end Alembic commands ###
