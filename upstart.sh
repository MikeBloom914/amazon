#!/usr/bin/env bash
chmod 755 *

python3 /root/monza/setup/schema.py
python3 /root/monza/setup/seed.py
python3 /root/monza/setup/makelist.py

#runtime
python3 /root/monza/run/wsgi.py

#Clear-up
rm -rf /root/monza/run/core/__pycache__
rm -rf /root/monza/run/core/controllers/__pycache__
