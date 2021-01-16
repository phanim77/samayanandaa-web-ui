# Generated by Django 2.1.1 on 2020-12-24 03:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('samayanandaa_web', '0002_auto_20200630_2311'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30, verbose_name='First name')),
                ('last_name', models.CharField(max_length=30, verbose_name='Last name')),
                ('email_addr', models.EmailField(max_length=254)),
                ('feedback_message_content', models.CharField(max_length=500)),
                ('created_time', models.DateTimeField()),
                ('modified_time', models.DateTimeField(null=True)),
                ('client_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='samayanandaa_web.NatalHoroscope')),
            ],
        ),
    ]