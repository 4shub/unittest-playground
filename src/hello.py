def open_file(directory):
	try:
		f = open(directory, 'r')
		return f
	except Exception as e:
		return e
