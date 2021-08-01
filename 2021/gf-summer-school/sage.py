from glif import Glif
from glif.gf import GFShellRaw
from glif.commands import Repr
from distutils.spawn import find_executable
import os
import subprocess

# Basically a unique string that will never show up in the output (hopefully)
COMMAND_SEPARATOR = "COMMAND_SEPARATOR===??!<>239'_"

class SageShell(object):
    def __init__(self):
        self.pipe = os.pipe()   # (read, write)
        self.gfproc = subprocess.Popen(('sage',),
                          stdin = subprocess.PIPE,
                          stderr = self.pipe[1],
                          stdout = self.pipe[1])
        self.commandcounter = 0
        self.infile = os.fdopen(self.pipe[0])

        # catch any initial messages
        sep = self.__writeSeparator()
        self.gfproc.stdin.flush()
        self.initialOutput = self.__getOutput(sep)

    def __writeCmd(self, cmd):
        if not cmd.endswith('\n'):
            cmd += '\n'
        self.gfproc.stdin.write(str.encode(cmd))
        self.commandcounter += 1

    def __writeSeparator(self):
        sep = COMMAND_SEPARATOR + str(self.commandcounter)
        self.gfproc.stdin.write(str.encode(f"print(\"{sep}\")\n"))
        return sep

    def __getOutput(self, sep):
        """ read lines until sep found """
        output = ""
        for line in self.infile:
            # if line.rstrip() == sep:
            if sep in line:
                return output
            output += line


    def handleLine(self, cmd):
        """ forwards a command to the GF Repl and returns the output """
        self.__writeCmd(cmd)
        sep = self.__writeSeparator()
        self.gfproc.stdin.flush()
        return self.__getOutput(sep)


glif = Glif()

# setup
for command in ['archive tmpGLIF/examples sage', 'import LexiconEng.gf', 'import LexiconSemantics.mmt']:
    print(command)
    print(glif.executeCommand(command))

gfshell2 = GFShellRaw(find_executable('gf'), cwd = glif.cwd)
print('import for second GF shell')
print(gfshell2.handle_command('import SageDTEng.gf'))

sageShell = SageShell()

while True:
    sentence = input('> ').strip()
    if not sentence:
        continue
    sentence = sentence[0].lower() + sentence[1:]
    if sentence[-1] in {'?', '.', '!'}:
        sentence = sentence[:-1].strip()
    sentence = sentence.replace('"', '\\"').replace('\\', '\\\\').replace('_', ' _ ')
    result = glif.executeCommand(f'ps -lexcode "{sentence}" | p -cat=Sentence | construct -view=LexiconSemantics')
    asts = [i.content[Repr.LOGIC_ELPI] for i in result.value.items]
    if not asts:
        print(result)
        continue
    for ast in asts:
        commands = gfshell2.handle_command(f'l {ast} | ps -unlexcode').strip().split('\n')
        for command in commands:
            command = command.replace('&+', '').replace('( ', '(').replace(' (', '(').replace(' .', '.')  # ' &+ ' is BIND token
            print('#', command)
            print(sageShell.handleLine(command).replace('sage: ', ''))
            print()

