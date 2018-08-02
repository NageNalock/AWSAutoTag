#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/8/2 下午6:30
# @Author  : Dicey
# @File    : S32AutotagVBucket.py
# @Software: PyCharm


from __future__ import print_function
import json
import boto3
import logging


'''
为 S3 自动打 tag 的 桶级别版本
S3 的 API 都已经在 CloudWatch 中给出
可以直接添加
'''

logger = logging.getLogger()
logger.setLevel(logging.INFO)


def lambda_handler(event, context):
    print("=========================")