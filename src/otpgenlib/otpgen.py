"""Module for generating HOTP and TOTP codes."""

import base64
import hashlib
import hmac
import struct
import time


def hotp(secret, interval):
    """Generate HOTP code."""
    # casefold=True so it works with both uppercase and lowercase characters
    key = base64.b32decode(secret, casefold=True)
    counter = struct.pack(">Q", interval)
    digest = hmac.new(key, counter, hashlib.sha1).digest()
    offset = digest[19] & 15
    unpk = struct.unpack(">I", digest[offset:offset + 4])[0]
    code = (unpk & 0x7FFFFFFF) % 1000000  # (10 ** 6)
    return code


def totp(secret, totp_time):
    """Generate TOTP code."""
    return hotp(secret, int(time.time()) // totp_time)
