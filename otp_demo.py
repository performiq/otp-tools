#!/usr/bin/env python3
#
# Demo from this link - https://github.com/pyauth/pyotp
#
# -----------------------------------------------------------------------------
"""



"""
# -----------------------------------------------------------------------------

import pyotp

totp = pyotp.TOTP("JBSWY3DPEHPK3PXP")

print(f"Current OTP: {totp.now()}")

