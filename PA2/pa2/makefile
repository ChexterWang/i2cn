CC=g++
CFLAG=-c
DBGFLAGS=-g
OPTFLAGS=-O2
STDFLAGS=-std=gnu11

all: SR SR.dbg

SR: hw2.c
	$(CC) $(STDFLAGS) $(OPTFLAGS) $< -o $@
SR.dbg: hw2.c
	$(CC) $(STDFLAGS) $(DBGFLAGS) $< -o $@

clean:
	rm -rf *.o SR SR.dbg
