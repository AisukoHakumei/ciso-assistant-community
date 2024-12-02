# Generated by Django 5.1.1 on 2024-12-02 19:45

import django.core.validators
import django.db.models.deletion
import iam.models
import uuid
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('core', '0044_qualification'),
        ('iam', '0009_create_allauth_emailaddress_objects'),
        ('tprm', '0003_entityassessment_representatives'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='EbiosRMStudy',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
                ('is_published', models.BooleanField(default=False, verbose_name='published')),
                ('name', models.CharField(max_length=200, verbose_name='Name')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Description')),
                ('eta', models.DateField(blank=True, null=True, verbose_name='ETA')),
                ('due_date', models.DateField(blank=True, null=True, verbose_name='Due date')),
                ('ref_id', models.CharField(max_length=100)),
                ('version', models.CharField(blank=True, default='1.0', help_text='Version of the Ebios RM study (eg. 1.0, 2.0, etc.)', max_length=100, null=True, verbose_name='Version')),
                ('status', models.CharField(blank=True, choices=[('planned', 'Planned'), ('in_progress', 'In progress'), ('in_review', 'In review'), ('done', 'Done'), ('deprecated', 'Deprecated')], default='planned', max_length=100, null=True, verbose_name='Status')),
                ('observation', models.TextField(blank=True, null=True, verbose_name='Observation')),
                ('assets', models.ManyToManyField(help_text='Assets that are pertinent to the study', related_name='ebios_rm_studies', to='core.asset', verbose_name='Assets')),
                ('authors', models.ManyToManyField(blank=True, related_name='authors', to=settings.AUTH_USER_MODEL, verbose_name='Authors')),
                ('compliance_assessments', models.ManyToManyField(help_text='Compliance assessments established as security baseline during workshop 1.4', related_name='ebios_rm_studies', to='core.complianceassessment', verbose_name='Compliance assessments')),
                ('folder', models.ForeignKey(default=iam.models.Folder.get_root_folder_id, on_delete=django.db.models.deletion.CASCADE, related_name='%(class)s_folder', to='iam.folder')),
                ('reviewers', models.ManyToManyField(blank=True, related_name='reviewers', to=settings.AUTH_USER_MODEL, verbose_name='Reviewers')),
                ('risk_assessments', models.ManyToManyField(help_text='Risk assessments generated at the end of workshop 4', related_name='ebios_rm_studies', to='core.riskassessment', verbose_name='Risk assessments')),
                ('risk_matrix', models.ForeignKey(help_text='Risk matrix used as a reference for the study. Defaults to `urn:intuitem:risk:library:risk-matrix-4x4-ebios-rm`', on_delete=django.db.models.deletion.PROTECT, related_name='ebios_rm_studies', to='core.riskmatrix', verbose_name='Risk matrix')),
            ],
            options={
                'verbose_name': 'Ebios RM Study',
                'verbose_name_plural': 'Ebios RM Studies',
                'ordering': ['created_at'],
            },
        ),
        migrations.CreateModel(
            name='AttackPath',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
                ('is_published', models.BooleanField(default=False, verbose_name='published')),
                ('description', models.TextField(verbose_name='Description')),
                ('is_selected', models.BooleanField(default=False, verbose_name='Is selected')),
                ('justification', models.TextField(blank=True, verbose_name='Justification')),
                ('ebios_rm_study', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ebios_rm.ebiosrmstudy', verbose_name='EBIOS RM study')),
            ],
            options={
                'verbose_name': 'Attack path',
                'verbose_name_plural': 'Attack paths',
                'ordering': ['created_at'],
            },
        ),
        migrations.CreateModel(
            name='FearedEvent',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
                ('is_published', models.BooleanField(default=False, verbose_name='published')),
                ('name', models.CharField(max_length=200, verbose_name='Name')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Description')),
                ('ref_id', models.CharField(max_length=100)),
                ('gravity', models.PositiveSmallIntegerField(default=0, verbose_name='Gravity')),
                ('is_selected', models.BooleanField(default=False, verbose_name='Is selected')),
                ('justification', models.TextField(blank=True, verbose_name='Justification')),
                ('assets', models.ManyToManyField(help_text='Assets that are affected by the feared event', related_name='feared_events', to='core.asset', verbose_name='Assets')),
                ('ebios_rm_study', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ebios_rm.ebiosrmstudy', verbose_name='EBIOS RM study')),
                ('qualifications', models.ManyToManyField(help_text='Qualifications carried by the feared event', related_name='feared_events', to='core.qualification', verbose_name='Qualifications')),
            ],
            options={
                'verbose_name': 'Feared event',
                'verbose_name_plural': 'Feared events',
                'ordering': ['created_at'],
            },
        ),
        migrations.CreateModel(
            name='OperationalScenario',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
                ('is_published', models.BooleanField(default=False, verbose_name='published')),
                ('description', models.TextField(verbose_name='Description')),
                ('likelihood', models.SmallIntegerField(default=-1, verbose_name='Likelihood')),
                ('is_selected', models.BooleanField(default=False, verbose_name='Is selected')),
                ('justification', models.TextField(blank=True, verbose_name='Justification')),
                ('attack_paths', models.ManyToManyField(help_text='Attack paths that are pertinent to the operational scenario', related_name='operational_scenarios', to='ebios_rm.attackpath', verbose_name='Attack paths')),
                ('ebios_rm_study', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='operational_scenarios', to='ebios_rm.ebiosrmstudy', verbose_name='EBIOS RM study')),
                ('threats', models.ManyToManyField(blank=True, help_text='Threats leveraged by the operational scenario', related_name='operational_scenarios', to='core.threat', verbose_name='Threats')),
            ],
            options={
                'verbose_name': 'Operational scenario',
                'verbose_name_plural': 'Operational scenarios',
                'ordering': ['created_at'],
            },
        ),
        migrations.CreateModel(
            name='ROTO',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
                ('is_published', models.BooleanField(default=False, verbose_name='published')),
                ('risk_origin', models.CharField(choices=[('state', 'State'), ('organized_crime', 'Organized crime'), ('terrorist', 'Terrorist'), ('activist', 'Activist'), ('professional', 'Professional'), ('amateur', 'Amateur'), ('avenger', 'Avenger'), ('pathological', 'Pathological')], max_length=32, verbose_name='Risk origin')),
                ('target_objective', models.CharField(max_length=200, verbose_name='Target objective')),
                ('motivation', models.PositiveSmallIntegerField(choices=[(0, 'undefined'), (1, 'very_low'), (2, 'low'), (3, 'significant'), (4, 'strong')], default=0, verbose_name='Motivation')),
                ('resources', models.PositiveSmallIntegerField(choices=[(0, 'undefined'), (1, 'limited'), (2, 'significant'), (3, 'important'), (4, 'unlimited')], default=0, verbose_name='Resources')),
                ('pertinence', models.PositiveSmallIntegerField(choices=[(0, 'undefined'), (1, 'irrelevant'), (2, 'partially_relevant'), (3, 'fairly_relevant'), (4, 'highly_relevant')], default=0, verbose_name='Pertinence')),
                ('activity', models.PositiveSmallIntegerField(default=0, validators=[django.core.validators.MaxValueValidator(4)], verbose_name='Activity')),
                ('is_selected', models.BooleanField(default=False, verbose_name='Is selected')),
                ('justification', models.TextField(blank=True, verbose_name='Justification')),
                ('ebios_rm_study', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ebios_rm.ebiosrmstudy', verbose_name='EBIOS RM study')),
                ('feared_events', models.ManyToManyField(related_name='ro_to_couples', to='ebios_rm.fearedevent', verbose_name='Feared events')),
            ],
            options={
                'verbose_name': 'RO/TO couple',
                'verbose_name_plural': 'RO/TO couples',
                'ordering': ['created_at'],
            },
        ),
        migrations.AddField(
            model_name='attackpath',
            name='ro_to_couple',
            field=models.ForeignKey(help_text='RO/TO couple from which the attach path is derived', on_delete=django.db.models.deletion.CASCADE, to='ebios_rm.roto', verbose_name='RO/TO couple'),
        ),
        migrations.CreateModel(
            name='Stakeholder',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
                ('is_published', models.BooleanField(default=False, verbose_name='published')),
                ('category', models.CharField(choices=[('client', 'Client'), ('partner', 'Partner'), ('supplier', 'Supplier')], max_length=32, verbose_name='Category')),
                ('current_dependency', models.PositiveSmallIntegerField(default=0, validators=[django.core.validators.MaxValueValidator(4)], verbose_name='Current dependency')),
                ('current_penetration', models.PositiveSmallIntegerField(default=0, validators=[django.core.validators.MaxValueValidator(4)], verbose_name='Current penetration')),
                ('current_maturity', models.PositiveSmallIntegerField(default=1, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(4)], verbose_name='Current maturity')),
                ('current_trust', models.PositiveSmallIntegerField(default=1, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(4)], verbose_name='Current trust')),
                ('residual_dependency', models.PositiveSmallIntegerField(default=0, validators=[django.core.validators.MaxValueValidator(4)], verbose_name='Residual dependency')),
                ('residual_penetration', models.PositiveSmallIntegerField(default=0, validators=[django.core.validators.MaxValueValidator(4)], verbose_name='Residual penetration')),
                ('residual_maturity', models.PositiveSmallIntegerField(default=1, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(4)], verbose_name='Residual maturity')),
                ('residual_trust', models.PositiveSmallIntegerField(default=1, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(4)], verbose_name='Residual trust')),
                ('is_selected', models.BooleanField(default=False, verbose_name='Is selected')),
                ('justification', models.TextField(blank=True, verbose_name='Justification')),
                ('applied_controls', models.ManyToManyField(blank=True, help_text='Controls applied to lower stakeholder criticality', related_name='stakeholders', to='core.appliedcontrol', verbose_name='Applied controls')),
                ('ebios_rm_studies', models.ManyToManyField(help_text='EBIOS RM studies in which the stakeholder is involved', related_name='stakeholders', to='ebios_rm.ebiosrmstudy', verbose_name='EBIOS RM studies')),
                ('entity', models.ForeignKey(help_text='Entity qualified by the stakeholder', on_delete=django.db.models.deletion.CASCADE, to='tprm.entity', verbose_name='Entity')),
            ],
            options={
                'verbose_name': 'Stakeholder',
                'verbose_name_plural': 'Stakeholders',
                'ordering': ['created_at'],
            },
        ),
        migrations.AddField(
            model_name='attackpath',
            name='stakeholders',
            field=models.ManyToManyField(help_text='Stakeholders leveraged by the attack path', related_name='attack_paths', to='ebios_rm.stakeholder', verbose_name='Stakeholders'),
        ),
    ]
