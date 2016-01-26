done=False

while not done:
	echo_txt = input("echo > ")
	if echo_txt == "bye":
		done = True
	elif echo_txt == "done":
		done = True
	else : 
		print(echo_txt)
else : 
	print("Good Bye")
