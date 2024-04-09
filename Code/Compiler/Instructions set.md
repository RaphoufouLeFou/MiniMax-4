# Memory Addressing

| Part  | Address    |
|-------|:-----------|
| RAM   | 0x00 - 0x07|
| REGA  | 0x08       |
| REGB  | 0x09       |
| RAR   | 0x0A       |
| RDR   | 0x0B       |
| TMPR  | 0x0C       |
| ORA   | 0x0D       |
| ORB   | 0x0E       |
| INR   | 0x0F       |

## ADD

```0001 RRRR xxxx```

## SUB

```0010 RRRR xxxx```

# JMP

```0011 DDDD DDxx```

# LDI

```0100 RRRR kkkk```

# MOV

```0101 RRRR PPPP```

# LD

```0110 AAAA xxxx```

# ST

```0111 AAAA xxxx```



add
sub
jmp
ldi
mov
ld
st
out
in
cp
breq
brne
halt
nop
