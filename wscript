#!/usr/bin/python3

def build(ctx):
    print('build')
    ctx(rule='mkdir -p il-86')
    ctx.recurse('models')

def install(ctx):
    pass

def configure(ctx):
    print('build')