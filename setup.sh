#!/bin/bash

virtualenv --no-site-packages --distribute .env && source .env/bin/activate && pip install -r requirements.txt
. ./.env/bin/activate # sources the activate file without creating a subshell
