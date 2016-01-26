import sys

def echo(in_, out):
	for line in in_:
		out.write(line)

def echo_2(in_, out):
	for line in in_:
		out.write("{0:04} {1}".format(len(line), line))

echo_2(sys.stdin,sys.stdout) 
