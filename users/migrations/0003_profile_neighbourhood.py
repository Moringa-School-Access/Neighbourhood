# Generated by Django 3.1.2 on 2020-11-02 07:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0002_auto_20201102_0059'),
        ('users', '0002_profile_bio'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='neighbourhood',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='members', to='project.neighbourhood'),
        ),
    ]
