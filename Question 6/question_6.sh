#!/bin/bash
#Bash script to delete all files in ./temp 14 days or older

find ./temp -type f -mtime +13 -exec rm -f {} +
