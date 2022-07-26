# otpgen

Module for generating HOTP and TOTP codes

## Table of Contents

- [Description](#description)
  - [Library Usage](#library-usage)
  - [Script Usage](#script-usage)
- [Contribution Guidelines](#contribution-guidelines)

## Description

This repository contains a library called otpgen which could be used to obtain
HOTP and TOTP codes, and an example script called totpgen.py, which is created
to demonstrate what the library can be used to create.

### Library Usage

To generate HOTP code from library:

```python
>>> from otpgenlib.otpgen import hotp
>>> hotp("<HOTP_SECRET>", <COUNT>)
```

To generate TOTP code from library:

```python
>>> from otpgenlib.otpgen import totp
>>> totp("<TOTP_SECRET", <COUNT>)
```

### Script Usage

To generate TOTP code from totpgen.py script:

```shell
$ totpgen.py "<TOTP_SECRET>"
$ # OR
$ echo "<TOTP_SECRET>" | totpgen.py -
```

**RECOMMENDATION:** Encrypt the file with the TOTP Secret using tools like
GnuPG, and pass its contents to the scripts.

```shell
$ totpgen.py "$(gpg -qd /file/with/totp/secret)"
$ # OR
$ gpg -qd /file/with/totp/secret | totpgen.py -
```

## Contribution Guidelines

See [CONTRIBUTING.md](CONTRIBUTING.md)
