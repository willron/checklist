# coding:utf-8
from __future__ import unicode_literals

from django.db import models
# Create your models here.


class CheckList(models.Model):
    name = models.CharField(max_length=100)
    first_step = models.OneToOneField('CheckListStep', null=True, related_name='checklistname', on_delete=models.DO_NOTHING)

    def __unicode__(self):
        return self.name


class CheckListStep(models.Model):
    checklist = models.ForeignKey(CheckList, null=True, related_name='step_list')
    content = models.CharField(max_length=100)
    next_step = models.OneToOneField('CheckListStep', null=True, related_name='last_step', on_delete=models.DO_NOTHING)
    parent_step = models.ForeignKey('CheckListStep', related_name='children_step', null=True)
    first_children = models.OneToOneField('CheckListStep', related_name='checkliststepparent', null=True, on_delete=models.DO_NOTHING)

    def __unicode__(self):
        return self.content

    def delete(self, *args, **kwargs):
        next_step_obj = self.next_step or None
        if self.checklist_id:
            if hasattr(self, 'checklistname'):
                obj = self.checklistname
                obj.first_step = next_step_obj
            else:
                obj = self.last_step
                obj.next_step = next_step_obj
        else:
            if hasattr(self, 'checkliststepparent'):
                obj = self.checkliststepparent
                obj.first_children = next_step_obj
            else:
                obj = self.last_step
                obj.next_step = next_step_obj
        result = super(CheckListStep, self).delete(*args, **kwargs)
        obj.save()
        return result
