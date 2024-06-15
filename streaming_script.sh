#!/bin/sh
# A lil script.
# 1. Make sure the destination file doesn't exist.

ROOT_DIR="dnv2011-hw1"

SCRIPT_DIR="~/hw1"
ARITY="1"
INPUT_DIR="$ROOT_DIR/data"
WORDCOUNT_OUTPUT_DIR="$ROOT_DIR/wc-output-$ARITY"
OUTPUT_DIR="$ROOT_DIR/output-$ARITY"

## WORDCOUNT
# Try to delete it if it already exists.
# Just errors if it doesn't work, which is fine.
hadoop fs -rm -r "$WORDCOUNT_OUTPUT_DIR"

# Okay, now let's count the words.
mapred streaming -input "$INPUT_DIR" -output "$WORDCOUNT_OUTPUT_DIR" \
		-mapper  "python $SCRIPT_DIR/hw1mapper.py -t"
		-reducer "python $SCRIPT_DIR/hw1totalreducer.py"

# That's good.
# hadoop fs -rm -r "$OUTPUT_DIR"
# mapred streaming -input "$INPUT_DIR" -output "$OUTPUT_DIR" \
#		-mapper "python $SCRIPT_DIR/hw1mapper.py"
#		-reducer "python $SCRIPT_DIR/hw1reducer.py"
