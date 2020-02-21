git submodule deinit -f $1
git rm $1
git config -f .gitmodules --remove-section $1
rm .git/modules/$1
rm -r $1
