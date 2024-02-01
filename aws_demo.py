#!/usr/bin/env python3
#
# See:
#
#  * https://github.com/pyauth/pyotp
#  * https://pyauth.github.io/pyotp/
#  * https://pypi.org/project/pyotp/
#
# -----------------------------------------------------------------------------
"""
Note:

  You will need to get an MFA secret - which can be obtained br
  decoding the QRCode used to set up the stream for an Authenticator
  application.

  For example the AWS IAM MFA QRCode has a link to display the
  enderlying URL which includes the MFS secret.

  Generally once you have added the stream to your auth app you
  will not be able to recover the SECRET.  You will need to replace
  the MFA setup with a new onei and extract the token before you
  setup you app.


"""
# -----------------------------------------------------------------------------

import os
import pyotp

try:
    AWS_MFA_SECRET = os.environ["AWS_MFA_SECRET"]

    totp = pyotp.TOTP(AWS_MFA_SECRET)

    print(f"Current OTP: {totp.now()}")

except Exception as ex:
    print(f"Something is wrong - {ex}")

