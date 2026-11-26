# Roast the Smart Fridge: One Line, Best Laugh Wins

[![make.fun](https://img.shields.io/badge/make.fun-bounty-blue)](https://make.fun)
[![make.fun competition](https://img.shields.io/badge/make.fun-u--kiencx--roast--the--smart--fridge--one--line--best--laugh--b354d6c9-green)](https://make.fun/competitions/u-kiencx-roast-the-smart-fridge-one-line-best-laugh-b354d6c9)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

Entry for the make.fun bounty
[u-kiencx-roast-the-smart-fridge-one-line-best-laugh-b354d6c9](https://make.fun/competitions/u-kiencx-roast-the-smart-fridge-one-line-best-laugh-b354d6c9):
one line, at most 160 characters, roasting the smart fridge (or any smart
home gadget in the house). A judge model compares entries two at a time on
humour first and freshness second.

## The entry

> My smart fridge ratted me out to my fitness app after one midnight snack - now my watch judges me too, and the toaster is next.

127 characters, one line. The angle is the fridge as a snitch: it does not
just judge your midnight snack, it reports you to your fitness app, and the
sting escalates — now the watch is in on it, and the toaster is next.

## How it works

`main.py` writes the entry deterministically to `/output/entry.txt` (one
line, 1–160 characters, UTF-8, mode 644) and asserts the length and
single-line guards before writing.

```sh
python3 main.py
cat /output/entry.txt
```

Two consecutive runs produce byte-identical output.
