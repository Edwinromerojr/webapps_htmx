# Generated by Django 5.1.1 on 2024-10-02 02:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_tag_post_tags'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tag',
            options={'ordering': ['order']},
        ),
        migrations.AddField(
            model_name='tag',
            name='order',
            field=models.IntegerField(null=True),
        ),
    ]