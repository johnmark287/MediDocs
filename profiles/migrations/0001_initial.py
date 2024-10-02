# Generated by Django 4.2 on 2024-03-08 12:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='HospitalProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Hospital Name')),
                ('createdAt', models.DateTimeField(auto_now_add=True, verbose_name='Date the hospital was added ')),
                ('updatedAt', models.DateTimeField(auto_now=True, verbose_name='Date the hospital details were updated ')),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region='KE')),
            ],
        ),
        migrations.CreateModel(
            name='HospitalService',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('category', models.CharField(choices=[('diagnostic', 'Diagnostic'), ('surgical', 'Surgical'), ('therapeutic', 'Therapeutic'), ('preventive', 'Preventive'), ('emergency', 'Emergency'), ('maternity', 'Maternity'), ('rehabilitation', 'Rehabilitation')], max_length=100)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('availability', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('address', models.TextField()),
                ('latitude', models.DecimalField(decimal_places=6, max_digits=9)),
                ('longitude', models.DecimalField(decimal_places=6, max_digits=9)),
            ],
        ),
        migrations.CreateModel(
            name='PatientProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_of_birth', models.DateField(verbose_name='Date of Birth')),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region='KE')),
                ('createdAt', models.DateTimeField(auto_now_add=True, verbose_name='Date the patient was added ')),
                ('updatedAt', models.DateTimeField(auto_now=True, verbose_name='Date the patient details were updated ')),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='patient', to='profiles.location', verbose_name='Location of the patient')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='patient_account_profile', to=settings.AUTH_USER_MODEL, verbose_name='User Account')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hospital_profile', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='profile_hospital', to='profiles.hospitalprofile', verbose_name='Hospital profile')),
                ('patient_profile', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='profile_patient', to='profiles.patientprofile', verbose_name='Patient profile')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL, verbose_name='User profile')),
            ],
        ),
        migrations.CreateModel(
            name='Nurse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('createdAt', models.DateTimeField(auto_now_add=True, verbose_name='Date the nurse was added ')),
                ('updatedAt', models.DateTimeField(auto_now=True, verbose_name='Date the nurse details were updated ')),
                ('hospital', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profiles.hospitalprofile')),
                ('name', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='hospitalprofile',
            name='location',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hospital', to='profiles.location', verbose_name='Location of the hospital'),
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('createdAt', models.DateTimeField(auto_now_add=True, verbose_name='Date the doctor was added ')),
                ('updatedAt', models.DateTimeField(auto_now=True, verbose_name='Date the doctor details were updated ')),
                ('hospital', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profiles.hospitalprofile')),
                ('name', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
