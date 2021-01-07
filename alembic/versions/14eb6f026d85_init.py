"""init

Revision ID: 14eb6f026d85
Revises:
Create Date: 2020-12-04 16:16:42.442007

"""
import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision = "14eb6f026d85"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "comment",
        sa.Column(
            "create_time",
            sa.DateTime(timezone=True),
            server_default=sa.text("now()"),
            nullable=True,
            comment="创建时间",
        ),
        sa.Column(
            "update_time",
            sa.DateTime(timezone=True),
            server_default=sa.text("now()"),
            nullable=True,
            comment="更新时间",
        ),
        sa.Column(
            "deleted",
            sa.Boolean(),
            server_default=sa.text("false"),
            nullable=False,
            comment="是否被删除",
        ),
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("user_id", sa.Integer(), nullable=False, comment="评论用户的 ID"),
        sa.Column("post_id", sa.Integer(), nullable=False, comment="Post 文章的 ID"),
        sa.Column("content", sa.Text(), nullable=False, comment="用户的评论"),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "post",
        sa.Column(
            "create_time",
            sa.DateTime(timezone=True),
            server_default=sa.text("now()"),
            nullable=True,
            comment="创建时间",
        ),
        sa.Column(
            "update_time",
            sa.DateTime(timezone=True),
            server_default=sa.text("now()"),
            nullable=True,
            comment="更新时间",
        ),
        sa.Column(
            "deleted",
            sa.Boolean(),
            server_default=sa.text("false"),
            nullable=False,
            comment="是否被删除",
        ),
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("topic_id", sa.Integer(), nullable=False, comment="文章所在的主题 ID"),
        sa.Column("user_id", sa.Integer(), nullable=False, comment="发布文章用户的 ID"),
        sa.Column("content", sa.Text(), nullable=False, comment="文章内容"),
        sa.Column(
            "click_times",
            sa.Integer(),
            server_default=sa.text("false"),
            nullable=True,
            comment="文章的点击数",
        ),
        sa.Column("tags", sa.JSON(), nullable=True, comment="文章的 tag"),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "root_topic",
        sa.Column(
            "create_time",
            sa.DateTime(timezone=True),
            server_default=sa.text("now()"),
            nullable=True,
            comment="创建时间",
        ),
        sa.Column(
            "update_time",
            sa.DateTime(timezone=True),
            server_default=sa.text("now()"),
            nullable=True,
            comment="更新时间",
        ),
        sa.Column(
            "deleted",
            sa.Boolean(),
            server_default=sa.text("false"),
            nullable=False,
            comment="是否被删除",
        ),
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("name", sa.String(length=256), nullable=False),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("name"),
    )
    op.create_table(
        "user",
        sa.Column(
            "create_time",
            sa.DateTime(timezone=True),
            server_default=sa.text("now()"),
            nullable=True,
            comment="创建时间",
        ),
        sa.Column(
            "update_time",
            sa.DateTime(timezone=True),
            server_default=sa.text("now()"),
            nullable=True,
            comment="更新时间",
        ),
        sa.Column(
            "deleted",
            sa.Boolean(),
            server_default=sa.text("false"),
            nullable=False,
            comment="是否被删除",
        ),
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("email", sa.String(length=100), nullable=False),
        sa.Column("password_hash", sa.String(length=256), nullable=False, comment="登陆密码 hash 之后的值"),
        sa.Column("name", sa.String(length=100), nullable=True),
        sa.Column("phone", sa.String(length=20), nullable=True, comment="电话号码"),
        sa.Column("avatar", sa.String(length=256), nullable=True, comment="用户头像"),
        sa.Column("website", sa.String(length=100), nullable=True, comment="个人网站"),
        sa.Column("company", sa.String(length=100), nullable=True, comment="所在公司"),
        sa.Column("job", sa.String(length=100), nullable=True, comment="职位"),
        sa.Column("location", sa.String(length=100), nullable=True, comment="所在地"),
        sa.Column("signature", sa.String(length=256), nullable=True, comment="签名"),
        sa.Column("dribbble", sa.String(length=256), nullable=True, comment="Dribbble"),
        sa.Column("duolingo", sa.String(length=256), nullable=True, comment="Duolingo"),
        sa.Column("about_me", sa.String(length=256), nullable=True, comment="About.me"),
        sa.Column("last_me", sa.String(length=256), nullable=True, comment="Last.fm"),
        sa.Column("good_reads", sa.String(length=256), nullable=True, comment="Goodreads"),
        sa.Column("github", sa.String(length=256), nullable=True, comment="GitHub"),
        sa.Column("psn_id", sa.String(length=256), nullable=True, comment="PSN ID"),
        sa.Column("stream_id", sa.String(length=256), nullable=True, comment="Steam_ID"),
        sa.Column("twitch", sa.String(length=256), nullable=True, comment="Twitch"),
        sa.Column("battle_tag", sa.String(length=256), nullable=True, comment="BattleTag"),
        sa.Column("instagram", sa.String(length=256), nullable=True, comment="Instagram"),
        sa.Column("telegram", sa.String(length=256), nullable=True, comment="Telegram"),
        sa.Column("twitter", sa.String(length=256), nullable=True, comment="Twitter"),
        sa.Column("btc_address", sa.String(length=256), nullable=True, comment="BTC Address"),
        sa.Column("coding_net", sa.String(length=256), nullable=True, comment="Coding.net"),
        sa.Column("personal_introduction", sa.String(length=256), nullable=True, comment="个人简介"),
        sa.Column("state_update_view_permission", sa.Integer(), nullable=True, comment="状态更新查看权限"),
        sa.Column("community_rich_rank", sa.Boolean(), nullable=True, comment="社区财富排行榜"),
        sa.Column("money", sa.Integer(), nullable=True, comment="余额"),
        sa.Column("show_remain_money", sa.Boolean(), nullable=True, comment="是否显示余额"),
        sa.Column(
            "use_avatar_for_favicon", sa.Boolean(), nullable=True, comment="使用节点头像作为页面 favicon"
        ),
        sa.Column("use_high_resolution_avatar", sa.Boolean(), nullable=True, comment="使用高精度头像"),
        sa.Column("time_zone", sa.String(length=256), nullable=True, comment="默认使用的时区"),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "topic",
        sa.Column(
            "create_time",
            sa.DateTime(timezone=True),
            server_default=sa.text("now()"),
            nullable=True,
            comment="创建时间",
        ),
        sa.Column(
            "update_time",
            sa.DateTime(timezone=True),
            server_default=sa.text("now()"),
            nullable=True,
            comment="更新时间",
        ),
        sa.Column(
            "deleted",
            sa.Boolean(),
            server_default=sa.text("false"),
            nullable=False,
            comment="是否被删除",
        ),
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("name", sa.String(length=256), nullable=False),
        sa.Column("root_topic_id", sa.Integer(), server_default=sa.text("1"), nullable=True),
        sa.ForeignKeyConstraint(
            ["root_topic_id"],
            ["root_topic.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("name"),
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("topic")
    op.drop_table("user")
    op.drop_table("root_topic")
    op.drop_table("post")
    op.drop_table("comment")
    # ### end Alembic commands ###
