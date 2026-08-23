#!/usr/bin/env bash

if (( $# != 2 )); then
	echo "Be sure to input the challenge year followed by the challenge day as script arguments.
Example:
./init-problem.sh 2015 1"
	exit 1
fi

year=$1
day=$2

cd ~/prog/aoc-python/ || exit 1
dir="$year/day$day"
mkdir -p "./$dir"
cd "$dir" || exit 1
cookie=$AOC_SESSION_COOKIE
wget "https://adventofcode.com/$year/day/$day/input" --header="Cookie: session=$cookie"
echo "Script returned exit code $?"
