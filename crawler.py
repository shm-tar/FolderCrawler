import os, fnmatch

dirs = [f for f in os.listdir(os.getcwd())]
# print(dirs)

pattern = "*.png"

for entry in dirs:
	try:
		files_in_dir = os.listdir(entry)
		
		for file_entry in files_in_dir:
			if fnmatch.fnmatch(file_entry, pattern):
				print(file_entry + " found!")
				input("Press any key to continue.")
				print("Removing " + file_entry)
				filename = os.path.join(os.getcwd(), entry, file_entry)
				os.remove(filename)
				print("Removed.")
	except(NotADirectoryError):
		pass
