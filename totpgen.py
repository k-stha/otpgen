#!/usr/bin/env python3

"""Generates TOTP codes and changes every 30 seconds."""

import sys
import time

from otpgen import totp

# Number of seconds for generating new code
COUNT = 30

if len(sys.argv) == 1:
    print("Please provide an argument!", file=sys.stderr)
    sys.exit()

i = 0

while i < len(sys.argv):
    arg = sys.argv[i]

    if arg in ("-h", "--help"):
        print(
            """\nUsage: totpgen.py [options] <OTP Seceret Code>\n
    Options:
      --help   :  Print this help menu
      --stdin  :  Take TOTP code from standard input\n"""
        )
        sys.exit()

    elif arg == "--stdin":
        SECRET = sys.stdin.read()

    else:
        SECRET = sys.argv[1]

    i += 1

# Making sure that the code works even if the user input has whitespaces
SECRET = SECRET.replace(" ", "").strip()

while True:  # Continue unless the user stops it
    print(
        "TOTP: "
        + str(totp(SECRET, COUNT)).zfill(6)
        + " | "
        + "Expires in "
        + str(COUNT - (time.time() % COUNT))
        + " seconds    ",
        end="\r",
    )
    # Spaces after "seconds" to clear previous text remaining in the console
    time.sleep(0.1)
