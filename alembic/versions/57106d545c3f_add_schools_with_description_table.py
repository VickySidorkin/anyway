"""Add schools with description table

Revision ID: 57106d545c3f
Revises: 7174ff899832
Create Date: 2019-08-13 19:46:21.054468

"""

# revision identifiers, used by Alembic.
revision = '57106d545c3f'
down_revision = '7174ff899832'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa
import geoalchemy2 as ga


def upgrade():
    op.create_table('schools_with_description',
    sa.Column('id', sa.BigInteger(), nullable=False),
    sa.Column('data_year', sa.Integer(), nullable=True),
    sa.Column('symbol_id', sa.Integer(), nullable=True),
    sa.Column('school_name', sa.Text(), nullable=True),
    sa.Column('students_number', sa.Integer(), nullable=True),
    sa.Column('municipality_name', sa.Text(), nullable=True),
    sa.Column('yishuv_name', sa.Text(), nullable=True),
    sa.Column('sector', sa.Text(), nullable=True),
    sa.Column('inspection', sa.Text(), nullable=True),
    sa.Column('legal_status', sa.Text(), nullable=True),
    sa.Column('reporter', sa.Text(), nullable=True),
    sa.Column('geo_district', sa.Text(), nullable=True),
    sa.Column('education_type', sa.Text(), nullable=True),
    sa.Column('school_type', sa.Text(), nullable=True),
    sa.Column('institution_type', sa.Text(), nullable=True),
    sa.Column('lowest_grade', sa.Integer(), nullable=True),
    sa.Column('highest_grade', sa.Integer(), nullable=True),
    sa.Column('foundation_year', sa.Integer(), nullable=True),
    sa.Column('location_accuracy', sa.Text(), nullable=True),
    sa.Column('geom', ga.types.Geometry(geometry_type='POINT', srid=4326), nullable=True),
    sa.Column('x', sa.Float(), nullable=True),
    sa.Column('y', sa.Float(), nullable=True),
    sa.Column('longitude', sa.Float(), nullable=True),
    sa.Column('latitude', sa.Float(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_schools_with_description_geom'), 'schools_with_description', ['geom'], unique=False)
    op.create_index(op.f('ix_schools_with_description_id'), 'schools_with_description', ['id'], unique=False)
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_schools_with_description_id'), table_name='schools_with_description')
    op.drop_index(op.f('ix_schools_with_description_geom'), table_name='schools_with_description')
    op.drop_table('schools_with_description')
    ### end Alembic commands ###