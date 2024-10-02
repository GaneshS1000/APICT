#!/bin/bash

## set/export pyenv vars
export PYENV_ROOT="$HOME/.pyenv"
export PATH="$PYENV_ROOT/bin:$PATH"
if command -v pyenv 1>/dev/null 2>&1; then
 eval "$(pyenv init --path)"
fi

#checking pyenv commands
pyenv versions

#Enable reqd python from pyenv
pyenv global 3.11.10
python -m venv myenv
source myenv/bin/activate
python -V
which python

#Verify files are downloaded
#ls -l

#install reqts pkgs
pip install -r ./requirements.txt

echo '###### Running API Tests#####'
pytest APIPetstoreTests  --junitxml=./xmlReport/output.xml

echo '## deactivate venv ##'
deactivate

echo '### reset the pyenv version to system python ###'
pyenv global system
