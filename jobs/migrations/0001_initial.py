# Generated by Django 3.0.2 on 2020-01-08 13:35

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0002_applicant'),
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.Customuser')),
            ],
        ),
    ]