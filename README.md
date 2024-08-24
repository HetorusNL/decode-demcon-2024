# Decode Demcon 2024

Repository with the [Decode Demcon 2024](https://mailing.demcon.com/lp/decode-demcon-challenge-festival-schedule-generator) implementation written in python.

## Installation

This program doesn't require any other dependencies than Python3 itself.
Any supported Python3 version should be sufficient to run the program.

## Usage

The input file `input.txt` is loaded by default, the content of the file can be modified to plan a different festival.
To use a different input file, pass the filename (either absolute or relative to repo root) to the `DemconFestivalPlanner` constructor in `main.py`.
The format of the entries of the input file must be as follows:

- `show_<show-id><whitespace><start-time><whitespace><end-time>`

An example show list is as follows:

- `show_1 1337 1338`
- `show_15   1    2`
- `show_2 2 3`

The program can be called as follows:

```bash
python3 main.py
```

Alternatively the program can be started with a debugger in VScode by pressing 'F5'.

## Example output

```
stage 1:
 * show 9: [ 1, 9 ]
 * show 28: [ 14, 21 ]
 * show 20: [ 22, 30 ]
 * show 25: [ 31, 38 ]
 * show 22: [ 42, 46 ]
stage 2:
 * show 11: [ 1, 4 ]
 * show 14: [ 5, 10 ]
 * show 5: [ 15, 20 ]
 * show 4: [ 26, 30 ]
 * show 30: [ 33, 36 ]
 * show 15: [ 37, 44 ]
stage 3:
 * show 2: [ 2, 9 ]
 * show 21: [ 15, 20 ]
 * show 13: [ 26, 29 ]
 * show 8: [ 30, 34 ]
 * show 19: [ 35, 44 ]
stage 4:
 * show 7: [ 2, 9 ]
 * show 24: [ 19, 23 ]
 * show 16: [ 27, 35 ]
 * show 17: [ 36, 39 ]
 * show 3: [ 44, 47 ]
stage 5:
 * show 12: [ 2, 11 ]
 * show 10: [ 20, 28 ]
 * show 1: [ 29, 33 ]
 * show 26: [ 37, 41 ]
stage 6:
 * show 18: [ 4, 10 ]
 * show 27: [ 30, 36 ]
stage 7:
 * show 29: [ 5, 13 ]
stage 8:
 * show 23: [ 6, 9 ]
stage 9:
 * show 6: [ 8, 15 ]
```

## License

MIT License, Copyright (c) 2024 Tim Klein Nijenhuis <tim@hetorus.nl>
