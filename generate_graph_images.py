import subprocess

subprocess.call(['quilt', 'pop', '-a'])

subprocess.check_call(
    ['dot', '-Tpng', 'oplog_applier/oplog_applier.gv', '-O'])

subprocess.check_call(
    ['mv', 'oplog_applier/oplog_applier.gv.png', '0_oplog_applier.png'])

for i, line in enumerate(
        subprocess.check_output(['quilt', 'series']).decode().split('\n')):

    if not line.strip():
        break

    patch_name = line.split('/')[-1]

    subprocess.check_call(['quilt', 'push'])

    subprocess.check_call(
        ['dot', '-Tpng', 'oplog_applier/oplog_applier.gv', '-O'])

    subprocess.check_call(
        ['mv', 'oplog_applier/oplog_applier.gv.png',
         f'{i + 1}_{patch_name}.png'])


subprocess.call(['quilt', 'pop', '-a'])
