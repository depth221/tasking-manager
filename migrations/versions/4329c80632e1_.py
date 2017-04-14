"""empty message

Revision ID: 4329c80632e1
Revises: a572dc09c774
Create Date: 2017-04-14 09:16:15.005313

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy import Integer


# revision identifiers, used by Alembic.
revision = '4329c80632e1'
down_revision = 'a572dc09c774'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('tags',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('organisations', sa.String(), nullable=True),
    sa.Column('campaigns', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('campaigns'),
    sa.UniqueConstraint('organisations')
    )
    op.add_column('projects', sa.Column('campaign_tag', sa.String(), nullable=True))
    op.add_column('projects', sa.Column('mapping_types', sa.ARRAY(Integer()), nullable=True))
    op.add_column('projects', sa.Column('organisation_tag', sa.String(), nullable=True))
    op.create_index(op.f('ix_projects_campaign_tag'), 'projects', ['campaign_tag'], unique=False)
    op.create_index(op.f('ix_projects_mapper_level'), 'projects', ['mapper_level'], unique=False)
    op.create_index(op.f('ix_projects_mapping_types'), 'projects', ['mapping_types'], unique=False)
    op.create_index(op.f('ix_projects_organisation_tag'), 'projects', ['organisation_tag'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_projects_organisation_tag'), table_name='projects')
    op.drop_index(op.f('ix_projects_mapping_types'), table_name='projects')
    op.drop_index(op.f('ix_projects_mapper_level'), table_name='projects')
    op.drop_index(op.f('ix_projects_campaign_tag'), table_name='projects')
    op.drop_column('projects', 'organisation_tag')
    op.drop_column('projects', 'mapping_types')
    op.drop_column('projects', 'campaign_tag')
    op.drop_table('tags')
    # ### end Alembic commands ###
