#!/bin/bash
venv_name="interval_merge"
conda create -n $venv_name python=3.8 -y
source activate $venv_name
pip install -r requirements.txt
python main.py