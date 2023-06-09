# Generated by Django 4.1.5 on 2023-02-01 04:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("tibblesapp", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="AuthGroup",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=150, unique=True)),
            ],
            options={"db_table": "auth_group", "managed": False,},
        ),
        migrations.CreateModel(
            name="AuthGroupPermissions",
            fields=[("id", models.BigAutoField(primary_key=True, serialize=False)),],
            options={"db_table": "auth_group_permissions", "managed": False,},
        ),
        migrations.CreateModel(
            name="AuthPermission",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255)),
                ("codename", models.CharField(max_length=100)),
            ],
            options={"db_table": "auth_permission", "managed": False,},
        ),
        migrations.CreateModel(
            name="AuthUser",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("password", models.CharField(max_length=128)),
                ("last_login", models.DateTimeField(blank=True, null=True)),
                ("is_superuser", models.IntegerField()),
                ("username", models.CharField(max_length=150, unique=True)),
                ("first_name", models.CharField(max_length=150)),
                ("last_name", models.CharField(max_length=150)),
                ("email", models.CharField(max_length=254)),
                ("is_staff", models.IntegerField()),
                ("is_active", models.IntegerField()),
                ("date_joined", models.DateTimeField()),
            ],
            options={"db_table": "auth_user", "managed": False,},
        ),
        migrations.CreateModel(
            name="AuthUserGroups",
            fields=[("id", models.BigAutoField(primary_key=True, serialize=False)),],
            options={"db_table": "auth_user_groups", "managed": False,},
        ),
        migrations.CreateModel(
            name="AuthUserUserPermissions",
            fields=[("id", models.BigAutoField(primary_key=True, serialize=False)),],
            options={"db_table": "auth_user_user_permissions", "managed": False,},
        ),
        migrations.CreateModel(
            name="Department",
            fields=[
                (
                    "d_no",
                    models.IntegerField(
                        db_column="D_NO", primary_key=True, serialize=False
                    ),
                ),
                (
                    "d_name",
                    models.CharField(
                        blank=True, db_column="D_NAME", max_length=50, null=True
                    ),
                ),
            ],
            options={"db_table": "department", "managed": False,},
        ),
        migrations.CreateModel(
            name="DjangoAdminLog",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("action_time", models.DateTimeField()),
                ("object_id", models.TextField(blank=True, null=True)),
                ("object_repr", models.CharField(max_length=200)),
                ("action_flag", models.PositiveSmallIntegerField()),
                ("change_message", models.TextField()),
            ],
            options={"db_table": "django_admin_log", "managed": False,},
        ),
        migrations.CreateModel(
            name="DjangoContentType",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("app_label", models.CharField(max_length=100)),
                ("model", models.CharField(max_length=100)),
            ],
            options={"db_table": "django_content_type", "managed": False,},
        ),
        migrations.CreateModel(
            name="DjangoMigrations",
            fields=[
                ("id", models.BigAutoField(primary_key=True, serialize=False)),
                ("app", models.CharField(max_length=255)),
                ("name", models.CharField(max_length=255)),
                ("applied", models.DateTimeField()),
            ],
            options={"db_table": "django_migrations", "managed": False,},
        ),
        migrations.CreateModel(
            name="DjangoSession",
            fields=[
                (
                    "session_key",
                    models.CharField(max_length=40, primary_key=True, serialize=False),
                ),
                ("session_data", models.TextField()),
                ("expire_date", models.DateTimeField()),
            ],
            options={"db_table": "django_session", "managed": False,},
        ),
        migrations.CreateModel(
            name="Faculty",
            fields=[
                (
                    "faculty_id",
                    models.IntegerField(
                        db_column="FACULTY_ID", primary_key=True, serialize=False
                    ),
                ),
                (
                    "faculty_name",
                    models.CharField(db_column="FACULTY_NAME", max_length=50),
                ),
                ("priority", models.CharField(db_column="Priority", max_length=1)),
            ],
            options={"db_table": "faculty", "managed": False,},
        ),
        migrations.CreateModel(
            name="PrefSlot",
            fields=[
                (
                    "day",
                    models.CharField(
                        db_column="DAY", max_length=9, primary_key=True, serialize=False
                    ),
                ),
            ],
            options={"db_table": "pref_slot", "managed": False,},
        ),
        migrations.CreateModel(
            name="Slot",
            fields=[
                ("day", models.CharField(db_column="DAY", max_length=9)),
                (
                    "slot_no",
                    models.IntegerField(
                        db_column="SLOT_NO", primary_key=True, serialize=False
                    ),
                ),
                ("hours", models.IntegerField(db_column="HOURS")),
                ("slot_starttime", models.TimeField(db_column="SLOT_STARTTIME")),
                ("slot_endtime", models.TimeField(db_column="SLOT_ENDTIME")),
            ],
            options={"db_table": "slot", "managed": False,},
        ),
        migrations.CreateModel(
            name="SlotAllocationSem3",
            fields=[
                (
                    "faculty_id",
                    models.IntegerField(blank=True, db_column="FACULTY_ID", null=True),
                ),
                (
                    "subject_code",
                    models.CharField(
                        blank=True, db_column="SUBJECT_CODE", max_length=50, null=True
                    ),
                ),
                (
                    "day",
                    models.CharField(
                        db_column="DAY", max_length=9, primary_key=True, serialize=False
                    ),
                ),
            ],
            options={"db_table": "slot_allocation_sem3", "managed": False,},
        ),
        migrations.CreateModel(
            name="Subject",
            fields=[
                (
                    "subject_code",
                    models.CharField(
                        db_column="SUBJECT_CODE",
                        max_length=50,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                (
                    "subject_name",
                    models.CharField(
                        blank=True, db_column="SUBJECT_NAME", max_length=50, null=True
                    ),
                ),
                (
                    "semester",
                    models.IntegerField(blank=True, db_column="SEMESTER", null=True),
                ),
                (
                    "hours_per_week",
                    models.IntegerField(
                        blank=True, db_column="HOURS_PER_WEEK", null=True
                    ),
                ),
            ],
            options={"db_table": "subject", "managed": False,},
        ),
        migrations.CreateModel(
            name="SubjectAllocations",
            fields=[
                (
                    "faculty_id",
                    models.IntegerField(
                        db_column="Faculty_ID", primary_key=True, serialize=False
                    ),
                ),
                (
                    "subject_code",
                    models.CharField(db_column="Subject_code", max_length=50),
                ),
            ],
            options={"db_table": "subject_allocations", "managed": False,},
        ),
        migrations.CreateModel(
            name="Timetable",
            fields=[
                (
                    "subject_code",
                    models.CharField(
                        db_column="SUBJECT_CODE",
                        max_length=50,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("slot_no", models.IntegerField(db_column="SLOT_NO")),
                (
                    "faculty_id",
                    models.IntegerField(blank=True, db_column="FACULTY_ID", null=True),
                ),
            ],
            options={"db_table": "timetable", "managed": False,},
        ),
        migrations.CreateModel(
            name="Users",
            fields=[
                ("name", models.CharField(db_column="Name", max_length=50)),
                ("d_no", models.IntegerField(db_column="D_NO")),
                (
                    "id",
                    models.IntegerField(
                        db_column="ID", primary_key=True, serialize=False
                    ),
                ),
                ("password", models.CharField(db_column="PASSWORD", max_length=50)),
            ],
            options={"db_table": "users", "managed": False,},
        ),
        migrations.CreateModel(
            name="displaydata",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("day", models.CharField(max_length=10)),
                ("timings", models.CharField(max_length=50)),
                ("subject_code", models.CharField(max_length=10)),
                ("faculty_name", models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name="PrefSub",
            fields=[
                (
                    "faculty",
                    models.OneToOneField(
                        db_column="FACULTY_ID",
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        primary_key=True,
                        serialize=False,
                        to="tibblesapp.faculty",
                    ),
                ),
            ],
            options={"db_table": "pref_sub", "managed": False,},
        ),
        migrations.DeleteModel(name="profilepic",),
    ]
