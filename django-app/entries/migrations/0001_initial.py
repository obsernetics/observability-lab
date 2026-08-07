from django.db import migrations, models

class Migration(migrations.Migration):
    initial = True
    dependencies = []
    operations = [
        migrations.CreateModel(
            name="Entry",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(max_length=80)),
                ("message", models.TextField(max_length=500)),
                ("created", models.DateTimeField(auto_now_add=True)),
            ],
            options={"ordering": ["-created"]},
        ),
    ]
