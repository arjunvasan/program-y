#!/usr/bin/env bash

python3 csv_to_aiml.py test.csv test.aiml

python3 aiml_to_csv.py test.aiml test2.csv
