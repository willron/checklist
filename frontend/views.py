#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
by:willron
"""
from django.shortcuts import render_to_response


def checklist_index(request):
    if request.method == 'GET':
        return render_to_response('checklists.html')
