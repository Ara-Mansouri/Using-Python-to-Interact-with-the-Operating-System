import os
os.listdir("new_dic")
['file2', 'dic2', 'dic1', 'file1.txt']
dic="new_dic"
for name in os.listdir(dic):
	 fullname=os.path.join(dic,name)
	 if os.path.isdir(fullname):
	 	print("{} is a directory".format(fullname))
         else:
		print("{} is a file".format(fullname))

new_dic/file2 is a file
new_dic/dic2 is a directory
new_dic/dic1 is a directory
new_dic/file1.txt is a file
#This is a simple python code showing what files and sub-directories are in a given directory.
