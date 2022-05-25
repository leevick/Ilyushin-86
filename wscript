#!/usr/bin/python3

def build(ctx):
    ctx(rule='bash -c "mkdir -p il-86/SimObjects/Airplanes/Ilyushin-86/model"')
    ctx.recurse('models')
    ctx.recurse('config')
    ctx.recurse('panel')
    ctx.recurse('texture')
    ctx.add_group()
    ctx(rule='bash -c "cp -rvf ../manifest.json ./il-86/manifest.json"',
        source='manifest.json', target='il-86/manifest.json')
    ctx(rule=f'python ../utils/generate_layout.py {ctx.path.abspath()}\\il-86')
    # print(ctx.path.abspath())


def clean(ctx):
    pass


def configure(ctx):
    ctx.env.CP = "cp"
    print('build')
