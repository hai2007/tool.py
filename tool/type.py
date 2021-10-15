#!/usr/bin/python3

# Number（数字）


def isInt(val):
    return type(val) == int


def isFloat(val):
    return type(val) == float


def isComplex(val):
    return type(val) == complex


def isNumber(val):
    return isInt(val) | isFloat(val) | isComplex(val)

# String（字符串）


def isString(val):
    return type(val) == str

# Tuple（元组）


def isTuple(val):
    return type(val) == tuple

# List（列表）


def isList(val):
    return type(val) == list

# Dictionary（字典）


def isDictionary(val):
    return type(val) == dict

# Set（集合）


def isSet(val):
    return type(val) == set
