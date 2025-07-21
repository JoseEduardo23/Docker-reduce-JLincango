#!/usr/bin/bash
mkdir -p splits
split -l 22 -d logs.txt splits/part_ --additional-suffix=.txt