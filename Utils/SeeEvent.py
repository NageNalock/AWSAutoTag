#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/7/16 上午11:30
# @Author  : Dicey
# @File    : SeeEvent.py
# @Software: PyCharm

from __future__ import print_function

import datetime
import boto3


# print('Loading function')

# ec2 = boto3.resource("ec2")
# iam = boto3.resource("iam")

def lambda_handler(event, context):
    import json
    tran(json.dumps(event, indent=2))


def tran(str_test):
    str2 = ""
    for s in str_test:
        if s == "'":
            str2 = str2 + "\""
        elif s == "," or s == "[" or s == "]" or s == "{" or s == "}":
            str2 = str2 + s + "\n" + "  "
        else:
            str2 = str2 + s
    print(str2)


if __name__ == '__main__':
    # event = {
    # "awslogs": {
    # "data": "H4sIAAAAAAAAAHWPwQqCQBCGX0Xm7EFtK+smZBEUgXoLCdMhFtKV3akI8d0bLYmibvPPN3wz00CJxmQnTO41whwWQRIctmEcB6sQbFC3CjW3XW8kxpOpP+OC22d1Wml1qZkQGtoMsScxaczKN3plG8zlaHIta5KqWsozoTYw3/djzwhpLwivWFGHGpAFe7DL68JlBUk+l7KSN7tCOEJ4M3/qOI49vMHj+zCKdlFqLaU2ZHV2a4Ct/an0/ivdX8oYc1UVX860fQDQiMdxRQEAAA=="
    # }
    # }
    # lambda_handler(event,"")

    tran()