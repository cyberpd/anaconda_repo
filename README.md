# anaconda_repo
anaconda repository list

<ul><li>download repodata.json</li></ul>
<pre>
wget -c -r --no-parent https://repo.continuum.io/pkgs/main/win-64/repodata2.json
wget -c -r --no-parent --regex-type pcre --accept-regex '(.\.json)' https://repo.continuum.io/pkgs/main/win-64/
wget -c -r --no-parent --regex-type pcre --accept-regex '(.\.json)' https://repo.continuum.io/pkgs/main/noarch/
wget -c -r --no-parent --regex-type pcre --accept-regex '(.\.json)' https://repo.continuum.io/pkgs/free/win-64/
wget -c -r --no-parent --regex-type pcre --accept-regex '(.\.json)' https://repo.continuum.io/pkgs/free/noarch/
</pre>

<ul><li>make download packages list (list.txt)</li></ul>
<pre>
cd '&ltlocal repository root&gt'
python repo_win-64_noarch.py
</pre>

<ul><li>download packages...</li></ul>
<pre>
wget -c -r -i list.txt
</pre>
