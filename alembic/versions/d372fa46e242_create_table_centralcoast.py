"""create_table_CentralCoast

Revision ID: d372fa46e242
Revises: 224d90d9d298
Create Date: 2024-04-24 11:26:15.539925

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision: str = 'd372fa46e242'
down_revision: Union[str, None] = '224d90d9d298'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('kingborough',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('app_num', sa.String(length=255), nullable=False),
    sa.Column('app_address', sa.String(length=255), nullable=True),
    sa.Column('advertised_date', sa.Integer(), nullable=True),
    sa.Column('closing_date', sa.Integer(), nullable=True),
    sa.Column('purpose', sa.String(length=255), nullable=True),
    sa.Column('documents', sa.Text(), nullable=True),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('now()'), nullable=True),
    sa.Column('updated_at', sa.DateTime(), server_default=sa.text('now()'), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('app_num')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('kalamunda',
    sa.Column('id', mysql.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('task_id', mysql.VARCHAR(length=255), nullable=True),
    sa.Column('app_number', mysql.VARCHAR(length=255), nullable=False),
    sa.Column('lodgement_date', mysql.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('description', mysql.TEXT(), nullable=True),
    sa.Column('applicant', mysql.TEXT(), nullable=True),
    sa.Column('name', mysql.VARCHAR(length=255), nullable=True),
    sa.Column('telephone', mysql.VARCHAR(length=255), nullable=True),
    sa.Column('email', mysql.TEXT(), nullable=True),
    sa.Column('decision', mysql.VARCHAR(length=255), nullable=True),
    sa.Column('decision_date', mysql.VARCHAR(length=255), nullable=True),
    sa.Column('stage_', mysql.VARCHAR(length=255), nullable=True),
    sa.Column('start_date', mysql.VARCHAR(length=255), nullable=True),
    sa.Column('end_date', mysql.VARCHAR(length=255), nullable=True),
    sa.Column('created_at', mysql.DATETIME(), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=True),
    sa.Column('updated_at', mysql.DATETIME(), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.create_index('app_number', 'kalamunda', ['app_number'], unique=True)
    op.drop_table('kingborough')
    # ### end Alembic commands ###
