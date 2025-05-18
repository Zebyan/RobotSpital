"""rename id_medicamente to id_medicament

Revision ID: 79e02be0b598
Revises: 0bcb15818fd3
Create Date: 2025-05-18 12:15:11.458167

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '79e02be0b598'
down_revision: Union[str, None] = '0bcb15818fd3'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.alter_column(
        'Medicamente',
        'id_medicamente',
        new_column_name='id_medicament',
        existing_type=sa.String(length=50),
        existing_nullable=False,
    )
    


def downgrade():
    # revert new_col → old_col
    op.alter_column(
        'Medicamente',
        'id_medicament',
        new_column_name='id_medicamente',
        existing_type=sa.String(length=255),
        existing_nullable=False
    )
