#!/bin/bash
#Script to find all files containing a phone number and output them to output.txt

grep -l -R --perl-regexp "\b(\(?\d{3}\)?\s*|\d{3}-)\d{3}-\d{4}\b" * > out.txt

