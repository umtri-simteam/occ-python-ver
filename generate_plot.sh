#!/bin/bash

PYTHON_SCRIPT="Python_occ_valid.py"


if [ ! -f "$PYTHON_SCRIPT" ]; then
  echo "Python script $PYTHON_SCRIPT not found!"
  exit 1
fi

for txt_file in *.txt; do
  if [ -f "$txt_file" ]; then

    if grep -qE '^[0-9]+(\.[0-9]+)?$' "$txt_file"; then
      echo "Processing $txt_file"
      

      python "$PYTHON_SCRIPT" "$txt_file"
      

      base_name=$(basename "$txt_file" .txt)
      

      mv plot.png "${base_name}_plot.png"
      mv statistics.csv "${base_name}_statistics.csv"
    else
      echo "Skipping $txt_file (contains non-numeric data)"
    fi
  else
    echo "No .txt files found in the current directory."
    exit 1
  fi
done

echo "Processing completed for all valid .txt files."
