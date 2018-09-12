import json
import re

repo_dir = (
	('repo.continuum.io/pkgs/main/win-64/', 'main_win-64'), 
	('repo.continuum.io/pkgs/main/noarch/', 'main_noarch'),
	('repo.continuum.io/pkgs/free/win-64/', 'free_win-64'),
	('repo.continuum.io/pkgs/free/noarch/', 'free_noarch')
)
			
def make_list(dir, file):
	with open(dir[0] + 'repodata.json') as data_file:
		data = json.load(data_file)	

	url = 'https://' + dir[0]
	p = re.compile('(.*python-2.*)|(.*python-3.[12345].*)|(.*py2[67].*)|(.*py3[45].*)')
	for list in data['packages']:	
		if p.match(list):
			print("rejected: " + list)
		else:
			#f.write("%s%s\n" % (url, list))
			file.write("%s%s\n" % (url, list))

file = open("list.txt","w+")
for dir in repo_dir:
	make_list(dir, file)
file.close()