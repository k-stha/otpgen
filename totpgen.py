#!/usr/bin/env python3

"""Generates TOTP codes and changes every 30 seconds."""

from os.path import basename
import sys
import time

from otpgen import totp


def return_help(script_name):
    """Return help text."""
    return (
        "Usage: "
        + script_name
        + " [OPTION...] [OTP Secret Code]\n\nOptions:\n"
        + "  -h, --help            Print this help menu\n"
        + "  -, --stdin            Take TOTP code from standard input"
    )


COUNT = 30    # Number of seconds for generating new code
SCRIPT_NAME = basename(sys.argv[0])
display_help = return_help(SCRIPT_NAME)

if len(sys.argv) == 1:
    print("Please provide an argument!\n", file=sys.stderr)
    print(display_help)
    sys.exit(1)

i = 0

while i < len(sys.argv):
    arg = sys.argv[i]

    if arg in {"-h", "--help"}:
        print(display_help)
        sys.exit()

    elif arg in {"-", "--stdin"}:
        SECRET = sys.stdin.read()

    else:
        SECRET = sys.argv[1]

    i += 1

# Making sure that the code works even if the user input has whitespaces
SECRET = SECRET.replace(" ", "").strip()

while True:  # Continue unless the user stops it
    try:
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

    except KeyboardInterrupt:
        sys.exit()

    except Exception:
        print("Unknown error occurred! Exiting...", file=sys.stderr)
        sys.exit(1)
