# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Profile'
        db.create_table('accounts_profile', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['auth.User'], unique=True)),
            ('short_info', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal('accounts', ['Profile'])

        # Adding model 'RegistrationProfile'
        db.create_table('accounts_registrationprofile', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'], unique=True)),
            ('activation_key', self.gf('django.db.models.fields.CharField')(max_length=40)),
        ))
        db.send_create_signal('accounts', ['RegistrationProfile'])

        # Adding model 'EmailVerification'
        db.create_table('accounts_emailverification', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('old_email', self.gf('django.db.models.fields.EmailField')(max_length=75)),
            ('new_email', self.gf('django.db.models.fields.EmailField')(max_length=75)),
            ('token', self.gf('django.db.models.fields.CharField')(default='b864c132-83d4-4fc4-868f-4c458030bda3', max_length=40)),
            ('code', self.gf('django.db.models.fields.CharField')(default='efb5cd02-ff1b-4879-a319-3fe3e4f07adc', max_length=40)),
            ('is_approved', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('is_expired', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('expiration_date', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2011, 1, 20, 19, 21, 27, 96003))),
        ))
        db.send_create_signal('accounts', ['EmailVerification'])


    def backwards(self, orm):
        
        # Deleting model 'Profile'
        db.delete_table('accounts_profile')

        # Deleting model 'RegistrationProfile'
        db.delete_table('accounts_registrationprofile')

        # Deleting model 'EmailVerification'
        db.delete_table('accounts_emailverification')


    models = {
        'accounts.emailverification': {
            'Meta': {'object_name': 'EmailVerification'},
            'code': ('django.db.models.fields.CharField', [], {'default': "'33657209-26cc-440a-b48c-1e85588e122b'", 'max_length': '40'}),
            'expiration_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2011, 1, 20, 19, 21, 27, 103303)'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_approved': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_expired': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'new_email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'old_email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'token': ('django.db.models.fields.CharField', [], {'default': "'b9e0b6fd-dd20-4dd4-9efe-03039070e98b'", 'max_length': '40'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        },
        'accounts.profile': {
            'Meta': {'object_name': 'Profile'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'short_info': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['auth.User']", 'unique': 'True'})
        },
        'accounts.registrationprofile': {
            'Meta': {'object_name': 'RegistrationProfile'},
            'activation_key': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'unique': 'True'})
        },
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['accounts']
