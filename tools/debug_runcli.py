import subprocess, sys
p = subprocess.Popen([sys.executable, 'src/app.py'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
cmds = """
load tests/resources/small_words.csv
contains hello
complete he 3
quit
"""
out, err = p.communicate(cmds)
print('STDOUT REPR:', repr(out))
print('LINES:', out.strip().splitlines())
print('ERR REPR:', repr(err))
