mkdir ~/.glone;

python3 -m pip install numpy;

cp ./glone.py ~/.glone/glone.py;

echo "{ \"account\":\"\", \"scm_url\":\"\" }" >> ~/.glone/config.json;

echo "rm -rf ~/.glone; sudo rm -f /bin/glone; rm -f remove.sh;" >> remove.sh;

chmod +x ./remove.sh;

printf "Build succeeded.\n"

sudo gcc glone.c -o /bin/glone;

