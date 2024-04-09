import sys, os

'''This program turns the asembly code into machine code.
Here is the available instructions:
add  -> 0001 RRRR xxxx
sub  -> 0010 RRRR xxxx
jmp  -> 0011 DDDD DDxx
ldi  -> 0100 RRRR kkkk
mov  -> 0101 RRRR PPPP
ld   -> 0110 RRRR AAAA
st   -> 0111 RRRR AAAA
cp   -> 1000 xxxx xxxx
breq -> 1001 DDDD DDxx
brne -> 1010 DDDD DDxx
halt -> 1011 xxxx xxxx
nop  -> 0000 xxxx xxxx

registers : 

REGA -> 0x08
REGB -> 0x09
RAR  -> 0x0A
RDR  -> 0x0B
TMPR -> 0x0C

RAM -> 0x00 to 0x07

'''


class lineClass:
    opcode = ""
    args = []

    def __init__(self, line):
        self.opcode = line[0]
        self.args = line[1:]
    


def parse_lines(lines: list[str]) -> list[lineClass]:
    lines2 = []
    for line in lines:
        l = parse_line(line)
        if l.opcode == "":
            continue
        lines2.append(l)
    return lines2

def parse_line(line: str) -> lineClass:
    line = line.upper()
    line = line.split(" ")
    return lineClass(line)

# Check if the file exists
if len(sys.argv) < 2:
    print("Usage: python Compiler.py <file>")
    sys.exit()
path = sys.argv[1]
if not os.path.exists(path):
    print("File not found")
    sys.exit()

with open(path, 'r') as file:
    code = file.read()

lines = code.split("\n")

lines2 = parse_lines(lines)
for liness in lines2:
    print(liness.opcode, liness.args)


a:str = 'abc'
print(a)
a = 5
print(a)


def calculate_arg(arg : str) -> int:
    if arg[0] == "0" and arg[1] == "X":
        return int(arg, 16)
    else:
        return int(arg)
    
def calculate_jmp_arg(arg : str) -> tuple[int, int]:
    if arg[0] == "0" and arg[1] == "X":
        return (int(arg[2:4], 16), int(arg[4:6], 16))
    else:
        return (int(arg[0:2]), int(arg[2:4]))

def resolve_args(arg : str) -> int:
    if arg == "REGA":
        return 0x08
    elif arg == "REGB":
        return 0x09
    elif arg == "RAR":
        return 0x0A
    elif arg == "RDR":
        return 0x0B
    elif arg == "TMPR":
        return 0x0C
    elif arg == "RAM0":
        return 0x00
    elif arg == "RAM1":
        return 0x01
    elif arg == "RAM2":
        return 0x02
    elif arg == "RAM3":
        return 0x03
    elif arg == "RAM4":
        return 0x04
    elif arg == "RAM5":
        return 0x05
    elif arg == "RAM6":
        return 0x06
    elif arg == "RAM7":
        return 0x07
    else:
        print("Error: Invalid argument : ", arg)
        return 0x00

def compile_line(line: lineClass) -> tuple[int, int, int]:
    if line.opcode == "ADD":
        return (0x01, resolve_args(line.args[0]), 0x00)
    elif line.opcode == "SUB":
        return (0x02, resolve_args(line.args[0]), 0x00)
    elif line.opcode == "JMP":
        return (0x03, calculate_arg(line.args[0]), 0x00)
    elif line.opcode == "LDI":
        return (0x04, resolve_args(line.args[0]), calculate_arg(line.args[1]))
    elif line.opcode == "MOV":
        return (0x05, resolve_args(line.args[0]), resolve_args(line.args[1]))
    elif line.opcode == "LD":
        return (0x06, resolve_args(line.args[0]), resolve_args(line.args[1]))
    elif line.opcode == "ST":
        return (0x07, resolve_args(line.args[0]), resolve_args(line.args[1]))
    elif line.opcode == "CP":
        return (0x08, calculate_arg(line.args[0]), 0x00)
    elif line.opcode == "BREQ":
        return (0x09, calculate_arg(line.args[0]), 0x00)
    elif line.opcode == "BRNE":
        return (0x0A, calculate_arg(line.args[0]), 0x00)
    elif line.opcode == "HALT":
        return (0x0B, 0x00, 0x00)
    elif line.opcode == "NOP":
        return (0x00, 0x00, 0x00)
    else:
        print("Error: Invalid opcode : ", line.opcode)
        return (0x00, 0x00, 0x00)

def compile_lines(lines: list[lineClass]) -> list[tuple[str, str, str]]:
    compiled = []
    for line in lines:
        compiled.append(compile_line(line))
    return compiled

def print_lines(lines: list[tuple[int, int, int]]):
    for line in lines:
        print(line)

compiled = compile_lines(lines2)
print_lines(compiled)
