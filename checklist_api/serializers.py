#!/usr/bin/env python
# -*- coding:utf-8 -*-

from rest_framework import serializers
from checklist_api.models import CheckList
from checklist_api.models import CheckListStep


class ChildrenStepSerializer(serializers.ModelSerializer):
    class Meta:
        model = CheckListStep
        fields = ('id', 'content', 'next_step')


class CheckListStepSerializer(serializers.ModelSerializer):
    children_step = ChildrenStepSerializer(many=True, read_only=True)

    class Meta:
        model = CheckListStep
        fields = ('id', 'content', 'next_step', 'first_children', 'children_step')


class CheckListSerializer(serializers.ModelSerializer):
    step_list = CheckListStepSerializer(many=True, read_only=True)

    class Meta:
        model = CheckList
        fields = ('id', 'name', 'first_step', 'step_list')


class CheckListShowSerializer(serializers.ModelSerializer):

    class Meta:
        model = CheckList
        fields = ('id', 'name')
