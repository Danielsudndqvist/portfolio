# Generated by Django 4.2.15 on 2025-02-23 14:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Education",
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
                ("institution", models.CharField(max_length=100)),
                ("degree", models.CharField(max_length=100)),
                ("field_of_study", models.CharField(max_length=100)),
                ("start_date", models.DateField()),
                ("end_date", models.DateField(blank=True, null=True)),
                ("description", models.TextField(blank=True)),
            ],
            options={
                "verbose_name_plural": "Education",
                "ordering": ["-end_date", "-start_date"],
            },
        ),
        migrations.CreateModel(
            name="Project",
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
                ("title", models.CharField(max_length=100)),
                ("slug", models.SlugField(blank=True, unique=True)),
                ("description", models.TextField()),
                ("short_description", models.CharField(max_length=200)),
                ("image", models.ImageField(blank=True, upload_to="projects/")),
                ("github_url", models.URLField(blank=True)),
                ("live_url", models.URLField(blank=True)),
                ("created_date", models.DateField()),
                ("featured", models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name="Technology",
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
                ("name", models.CharField(max_length=50)),
                (
                    "icon",
                    models.CharField(
                        blank=True, help_text="FontAwesome icon class", max_length=50
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "Technologies",
            },
        ),
        migrations.CreateModel(
            name="WorkExperience",
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
                ("company", models.CharField(max_length=100)),
                ("position", models.CharField(max_length=100)),
                ("location", models.CharField(max_length=100)),
                ("start_date", models.DateField()),
                ("end_date", models.DateField(blank=True, null=True)),
                ("description", models.TextField()),
                ("technologies_used", models.ManyToManyField(to="projects.technology")),
            ],
            options={
                "ordering": ["-end_date", "-start_date"],
            },
        ),
        migrations.CreateModel(
            name="ProjectImage",
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
                ("image", models.ImageField(upload_to="projects/gallery/")),
                ("caption", models.CharField(blank=True, max_length=200)),
                (
                    "project",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="additional_images",
                        to="projects.project",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="project",
            name="technologies",
            field=models.ManyToManyField(to="projects.technology"),
        ),
    ]
