#!/usr/bin/env python3

challenge= ["science", "turbo", ["goggles", "eyes"], "nothing"]


trial= ["science", "turbo", {"eyes": "goggles", "goggles": "eyes"}, "nothing"]


nightmare= [{"slappy": "a", "text": "b", "kumquat": "goggles", "user":{"awesome": "c", "name": {"first": "eyes", "last": "toes"}},"banana": 15, "d": "nothing"}]

print(" My", challenge[2][1],"! The ", challenge[2][0], "do", challenge[3])

print(" My", trial[2] ,"! The ", trial.key(), "do", trial[3])

print(" My", challenge,"! The ", trial, "do", nightmare)
