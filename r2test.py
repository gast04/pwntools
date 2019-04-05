from pwn import *
context.terminal = ["xfce4-terminal", "--disable-server", "-e"]
p = process("less")
gdb.attach(p, r2cmd="db 0x1234")
#gdb.attach(p)
