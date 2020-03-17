import os, fnmatch
from send2trash import send2trash

dirs = [f for f in os.listdir(os.getcwd())]

pattern = "*.png"
deletes = []

for folder_entry in dirs:
	try:
		files_in_dir = os.listdir(folder_entry)
		for file_entry in files_in_dir:
			if fnmatch.fnmatch(file_entry, pattern):
				deletes.append(os.path.join(os.getcwd(), folder_entry, file_entry))
	except(NotADirectoryError):
		pass

if len(deletes) == 0:
	raise Exception(f"No files with {pattern} extension found.")

for i in deletes:
	print(i)

input("\nPress any key to remove files.\n")
try:
	for i in deletes:
		send2trash(i)
	print("Removed files successfully.")
except Exception as e:
	raise Exception(e)
