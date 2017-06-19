#!/usr/bin/env bash
uwsgi --http :8000 --module project_base.wsgi
