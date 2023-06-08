# Generated by Django 4.1 on 2023-06-07 12:52

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('books', '0002_author_slug'),
        ('api_overview', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CartItems',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('ordered_when', models.DateTimeField(auto_now_add=True)),
                ('cost_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('shipping_fee', models.DecimalField(decimal_places=2, max_digits=10)),
                ('total_paid', models.DecimalField(decimal_places=2, max_digits=10)),
                ('delivered', models.BooleanField(default=False)),
                ('item_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='books.booksmodel')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api_overview.profile')),
            ],
        ),
    ]