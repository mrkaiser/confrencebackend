confrencebackend
================

Flask backend for our conference app

##NOTE
Python 3.3.3 is the current testbed.

##SETUP
###Installing python
####Ubuntu
`sudo apt-get install python3` NOTE: Do not install any uncessary python packages via the APT repository. That can be handled by pip

Check your link `which python`. `cd` into that directory. `ll python` if the link isn't pointing to python3
    
    $ rm python
    $ ln -s $(which python3) python
    $ python --version 
    >> Python 3.3.2 (or whatever it maybe)

###Install pip
    
    $ wget --no-certificate https://raw.github.com/pypa/pip/master/contrib/get-pip.py
    $ python get-pip.py

###Installing virtualenv virtualenvwrapper
Make sure pip works with python3: `pip --version`
    
    pip install virtualenv virtualenvwrapper

To create a virtualenv
    
    $ mkvirtualenv dcenv
    (dceenv) $ deactivate
    $ 

Put these three lines in either your `.bashrc` or `.zshrc`

    export WORKON_HOME=$HOME/.virtualenvs
    export PROJECT_HOME=$HOME/Devel
    source /usr/local/bin/virtualenvwrapper.sh

###Setting up MySQL

    sudo apt-get install mysql5.5

Create a test database in mysql and `GRANT ALL` on a dummy user


###Setup the virtualenv

Within your virtualenv 

    sudo pip install --allow-external mysql-connector-python mysql-connector-python
    sudo pip install -r requirements.txt 

will install all the necessary components. 