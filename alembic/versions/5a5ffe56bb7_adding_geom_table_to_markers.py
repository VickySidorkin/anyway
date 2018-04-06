"""Adding geom table to markers

Revision ID: 5a5ffe56bb7
Revises: 3c0d35fdbe2e
Create Date: 2018-03-07 13:49:06.780319

"""
from geoalchemy2.types import Geometry

# revision identifiers, used by Alembic.
revision = '5a5ffe56bb7'
down_revision = '3c0d35fdbe2e'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    conn = op.get_bind()
    conn.execution_options(isolation_level="AUTOCOMMIT")
    conn.execute('CREATE EXTENSION postgis;')
    conn.execute('CREATE EXTENSION postgis_topology;')
    conn.execute("SELECT AddGeometryColumn('public','markers','geom',4326,'POINT',2);")
    conn.execute('UPDATE markers SET geom = ST_SetSRID(ST_MakePoint(longitude,latitude),4326);')
    conn.execute('CREATE INDEX idx_markers_geom ON markers USING GIST(geom);')
    conn.execute('VACUUM ANALYZE')

    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    conn = op.get_bind()
    conn.execution_options(isolation_level="AUTOCOMMIT")
    conn.execute('DROP INDEX idx_markers_geom;')
    op.drop_column('markers', 'geom')
    conn.execute('DROP EXTENSION postgis_topology;')
    conn.execute('DROP EXTENSION postgis;')
    conn.execute('DROP SCHEMA IF EXISTS topology CASCADE;')
    conn.execute('VACUUM ANALYZE')
    ### end Alembic commands ###