"""create core tables

Revision ID: 20260803_0001
Revises:
Create Date: 2026-08-03 00:00:00

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = "20260803_0001"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "users",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("phone_number", sa.String(length=32), nullable=False),
        sa.Column("real_number", sa.String(length=32), nullable=False),
        sa.Column("plan", sa.String(length=32), nullable=False),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("phone_number"),
    )
    op.create_index(op.f("ix_users_id"), "users", ["id"], unique=False)

    op.create_table(
        "agent_config",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("user_id", sa.Integer(), nullable=False),
        sa.Column("persona_prompt", sa.Text(), nullable=False),
        sa.Column("spam_rules", sa.Text(), nullable=True),
        sa.Column("voice_id", sa.String(length=128), nullable=True),
        sa.ForeignKeyConstraint(["user_id"], ["users.id"], ondelete="CASCADE"),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("user_id"),
    )
    op.create_index(op.f("ix_agent_config_id"), "agent_config", ["id"], unique=False)

    op.create_table(
        "calls",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("user_id", sa.Integer(), nullable=False),
        sa.Column("caller_number", sa.String(length=32), nullable=False),
        sa.Column("transcript", sa.Text(), nullable=True),
        sa.Column("outcome", sa.String(length=255), nullable=True),
        sa.Column("timestamp", sa.DateTime(timezone=True), server_default=sa.func.now(), nullable=False),
        sa.ForeignKeyConstraint(["user_id"], ["users.id"], ondelete="CASCADE"),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(op.f("ix_calls_id"), "calls", ["id"], unique=False)


def downgrade() -> None:
    op.drop_index(op.f("ix_calls_id"), table_name="calls")
    op.drop_table("calls")

    op.drop_index(op.f("ix_agent_config_id"), table_name="agent_config")
    op.drop_table("agent_config")

    op.drop_index(op.f("ix_users_id"), table_name="users")
    op.drop_table("users")
