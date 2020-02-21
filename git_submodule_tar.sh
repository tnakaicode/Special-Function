# git archive HEAD $1 --output=${HOME}/tmp/$2.tar.zip
git archive HEAD $1 --output=${HOME}/tmp/$2.tar.gz

ls -la ${HOME}/tmp/
