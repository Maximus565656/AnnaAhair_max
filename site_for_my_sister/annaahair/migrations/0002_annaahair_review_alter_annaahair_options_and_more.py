# Generated by Django 4.1.4 on 2022-12-11 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('annaahair', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Annaahair_review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Имя пользователя:')),
                ('review', models.TextField(verbose_name='Комментарий:')),
            ],
            options={
                'verbose_name': 'Комментарий',
                'verbose_name_plural': 'Комментарий',
                'ordering': ['-title'],
            },
        ),
        migrations.AlterModelOptions(
            name='annaahair',
            options={'ordering': ['-title'], 'verbose_name': 'Блог', 'verbose_name_plural': 'Информация'},
        ),
        migrations.AlterField(
            model_name='annaahair',
            name='review',
            field=models.TextField(verbose_name='Текст:'),
        ),
        migrations.AlterField(
            model_name='annaahair',
            name='title',
            field=models.CharField(max_length=50, verbose_name='Заголовок:'),
        ),
    ]
