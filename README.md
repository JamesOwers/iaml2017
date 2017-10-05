# Introductory applied machine learning (INFR10069)

These instructions are written for set up on DICE / a Unix environment.

**Distance learners please note**:
We recommend two options for working remotely. We preference that you use your
own machine:

1. Use your own machine! Conda installation should work fine on your own
computer. You must still have a DICE account: when submitting assignments, you
will need to copy work up to DICE and submit from there. Instructions will be
given for this in each assignment
1. Use virtual dice - a virtual machine emulated on your own computer connected
to the dice network. Please read here for installation instructions and more:
http://computing.help.inf.ed.ac.uk/vdice

**Windows users please note**:
* After conda installation, all instructions are much the same
* please follow conda installation instructions on their
website [here](https://conda.io/docs/user-guide/install/index.html)
* to activate the `iaml` environment, note that you don't type `source activate iaml`
but instead just `activate iaml`
* you can ignore section 3b (though you can google windows equivalents of all
  the Unix commands given)

# Setting up on DICE or Unix

Within this course we will be using Python along with a few open-source
libraries (packages). We will be using a virtual environment and package
management tool called [conda](https://conda.io/docs/).

We're going to run the entire setup in the terminal. If you're on a DICE
machine, click Applications in the top left, go to Utilities, then click
Terminal.

In the below instructions, any text styled `like this` should be executed in
the terminal. We are expecting you to enter these commands in **by hand
one-by-one**. This is for pedagogical reasons, and to help detect new issues.
Please read and heed any warnings *and especially errors* you may encounter. We
are on standby in the labs to help if required.

## 1. Check your available space
Firstly, please note that your space on DICE is allocated dynamically. If you are
having problems it may be because you were using new space faster than it could
be allocated to you!

All DICE users **registered** for IAML will automatically be allocated **20GB**
extra space over their default space values. **Please register for the course
ASAP to get this space**.
1. Check how much space you have on DICE. **You will need at least 4.5GB**.
    1. `freespace`
    1. If you don't have enough space, follow the instructions on [this page](
        http://computing.help.inf.ed.ac.uk/afs-quotas)

## 2. If you don't have it - Install conda
1. **Check you don't already have conda installed!**
    1. `which conda`
    1. **if you already have it installed, skip ahead to Create an Environment**
    1. It doesn't matter if you have miniconda2, miniconda3, anaconda2, or
    anaconda3 installed - they will all work for this course
1. If you don't have conda, download the latest version of miniconda2
    1. `cd ~/Downloads` (you can make a Downloads folder if you don't have one)
    1. Download the installer, depending on your system (you can check links [here](https://conda.io/miniconda.html)):
        * Linux: `wget https://repo.continuum.io/miniconda/Miniconda2-latest-Linux-x86_64.sh`
        * Mac: `wget https://repo.continuum.io/miniconda/Miniconda2-latest-MacOSX-x86_64.sh` or `curl -LOk https://repo.continuum.io/miniconda/Miniconda2-latest-MacOSX-x86_64.sh`
        * Or just simply download from [the site](https://conda.io/miniconda.html)
1. Install miniconda2 *with default settings*
    1. `bash Miniconda2-latest-Linux-x86_64.sh`
    1. Follow the prompt - **type `yes` and hit `enter` to accept all default
    settings when asked**
1. Close Terminal and reopen
1. Try executing `conda -h`. If it works, you can delete the installer
`rm ~/Downloads/Miniconda2-latest-Linux-x86_64.sh`

## 3a. Create an environment for IAML
1. Update conda: `conda update conda` (at the time of writing, the latest
  version was 4.3.25, but you should be safe to use later versions)
1. Create the environment for the course. Call it iaml and install python 2:
`conda create --name iaml python=2`

## 3b. Err...what's an environment?
An environment is a collection of packages of specific versions. You can have
multiple environments and switch between them for different projects. Conda is
a tool for managing both environments *and* the packages within each
environment. Here's a quick intro:

1. Show a list of your environments: `conda env list`
1. Print `$PATH`, one of your system's [environment variables](https://en.wikipedia.org/wiki/Environment_variable), in the
terminal: `echo $PATH`
    * `$PATH` is the list of directories your terminal can search to find
anything you execute:
1. Print a list of python installations on your `$PATH` (the top one is the one
    that will get executed if you type `python` in the terminal):
    `which python -a`
1. Activate the new environment: `source activate iaml`
1. Show list of python installations on your system *now*: `which python -a`
1. Show your system `$PATH` again: `echo $PATH`
1. Deactivate the new environment: `source deactivate`
1. Observer how your $PATH has changed again: `echo $PATH`
1. Make an empty environment: `conda create --name empty`
1. You can clone environments; this is useful for backing up: `conda create
--name empty_bkp --clone empty`
1. Make a python 3 environment with numpy already installed: `conda create
--name py3 python=3 numpy`
1. `conda env list`
1. Activate py3: `source activate py3`
1. Show the installed packages: `conda list`
1. Switch environments: `source deactivate; source activate empty`
1. `conda list` to show packages (note that python and, crucially,
    [pip](https://pip.pypa.io/en/stable/) are not installed)
1. Q: What python would get used now? `which python` A: the conda root
environment installation of python i.e. *not* this environment's python.
1. Install numpy: `conda install numpy`
1. Q: What python would get used *now*? `which python` A: You may have clocked
that conda installed a dependency of numpy (a python package)...python!
1. Let's delete these test environments:
    * `source deactivate`
    * `conda env list`
    * `conda remove --name empty --all`
    * `conda remove --name empty_bkp --all`
    * `conda remove --name py3 --all`
    * `conda env list`

## 4. Install all the packages for IAML
1. Activate the environment: `source activate iaml`
1. {May take 5 minutes} Install all required packages: `conda install jupyter=1.0.0 matplotlib=2.0.2 pandas=0.20.3 numpy=1.13.1 scikit-learn=0.19.0 scipy=0.19.1 seaborn=0.8`
    * Please note that normally we wouldn't specify the version numbers. Conda
    automatically downloads the most recent **consistent** set of packages.
    We specify versions here such that this course is consistent regardless of
    when you start (/recreate your environment!)
1. Get some space back: `conda clean -a`

### *IMPORTANT*
Before starting any IAML work in a new terminal **you must always activate the
iaml conda environment** using `source activate iaml`. If the environment is not
activated, you will be using your base python with its own set of packages. If
you are ever in any doubt of which python version is being used, execute
`which python`.

## 5. Get course material

You should now have all the required modules installed. Our next step is to make
a new directory where we will keep all the lab notebooks, datasets and
assignments. Within your terminal:

1. Navigate back to your home directory: `cd`
2. Make a new directory and navigate to it
    * `mkdir iaml_2017`
    * `cd iaml_2017`

Now you have two options:

1. We recommend that you directly download a .zip file from https://github.com/JamesOwers/iaml2017 which will contain everything you need and
save it in the folder you have just created. You can do this from the terminal
by typing:
    * `wget https://github.com/JamesOwers/iaml2017/archive/master.zip`
    * `unzip master.zip`
1. If **and only if** you are familiar and confident with using Git/GitHub, you
can initialize a git directory, add the above repo as remote and pull everything
into your local directory

### *IMPORTANT*
Supporting and teaching git is not in scope for this course so please only do
this if you are happy to google your own solutions!

## 6. Get started!!!
Once you have downloaded the material, you are now ready to start working with
Jupyter notebooks. First you need to activate the software environment and then
start a Jupyter Notebook session from within the folder where the material is
stored. *You will have to follow this procedure for all labs and assignments.*

1. Activate the conda environment: `source activate iaml`
2. Enter the directory where you downloaded the course material:
`cd iaml_2017/iaml-master`
3. Start a jupyter notebook
    * `jupyter notebook`
4. This should automatically open your browser
    * Click on `01_Lab_0_Introduction.ipynb` to open it

## Further Reading

- Conda getting started - 30 minute practical well worth going through https://conda.io/docs/user-guide/getting-started.html
- System Environment variables - https://en.wikipedia.org/wiki/Environment_variable
- Linux execution order - https://www.cyberciti.biz/tips/how-linux-or-unix-understand-which-program-to-run-part-i.html

## Troubleshooting

### I ran out of space when installing packages

Firstly, please note that your space on DICE is allocated dynamically. If you are
having problems it may be because you were using new space faster than it could
be allocated to you!
1. Check how much space you have on DICE. **You will need at least 4.5GB**.
    1. `freespace`
    1. If you don't have enough space, follow the instructions on [this page](
        http://computing.help.inf.ed.ac.uk/afs-quotas)
1. Try instaling packages individually and executing `conda clean --all` after
each installation

### Trashing your environment
If you install incorrect packages, or a package breaks for some reason, you can
just delete your environment and start again. Execute `conda remove --name iaml
--all` then install the package as described above.

### Trashing your whole conda installation
This is fairly extreme but as a final resort can be done quickly and easily.
Please note that you will lose *all* your environments if you do this, so check
this will not affect you before proceeding...[follow instructions here](https://conda.io/docs/user-guide/install/linux.html?highlight=uninstall#uninstalling-anaconda-or-miniconda)

### Unzipping master.zip error
Check that you downloaded the zip correctly! An error like:
```
End-of-central-directory signature not found.  Either this file is not
  a zipfile, or it constitutes one disk of a multi-part archive.  In the
  latter case the central directory and zipfile comment will be found on
  the last disk(s) of this archive.
```
means that the file you've downloaded is likely incomplete. Try downloading from
the [GitHub repo](https://github.com/JamesOwers/iaml2017) directly by clicking the green button and downloading the zip.

### wget: command not found
You do not have wget installed! Either install it, download from
the [GitHub repo](https://github.com/JamesOwers/iaml2017) directly by clicking the green button and download the zip, or try using another program like curl e.g. `curl -LOk https://github.com/JamesOwers/iaml2017/archive/master.zip`

### conda: command not found or 'Conda never works in new terminal'
DICE issue: DICE has a different set of bash startup mechanism, and you may need
to edit some different files yourself. **Do the below with ~/.benv instead**. See [here](http://computing.help.inf.ed.ac.uk/dice-bash) for more info.

Unix solution: First try closing your terminal and reopening. If that doesn't fix, it's likely that, in the conda installation, you didn't allow conda to add the it's bin directory to your $PATH. Check your home directory for `~/.bashrc` or `~/.bash_profile`. You should have a line in one of those files that looks like this:
```
# added by Miniconda2 4.3.21 installer
export PATH="/afs/inf.ed.ac.uk/user/s12/s1234567/miniconda2/bin:$PATH"
```
If you don't, you can add it like this (changing the conda installation location line):
```
miniconda_location=/afs/inf.ed.ac.uk/user/s12/s1234567/miniconda2/bin
echo 'export PATH=:$PATH' >>~/.bash_profile
```

### 'source' is not recognized as an internal or external command, ...
You're on windows aren't you! Please see the note at the top of the file (you
can omit `source`)

### 'which' is not recognized as an internal or external command, ...
You're on windows aren't you! Please see the note at the top of the file (
`which` = `where` on windows).

### $PATH?
You're on windows aren't you! Please see the note at the top of the file (
`echo $PATH` == `echo %PATH%` on windows).

### I can't find my conda environment....but I definitely created it
We have found that people also taking MLP and/or ANLP (other courses that use
conda) have installed multiple versions of conda. To check whether you've done
this, simply list your home directory:

```{bash}
ls ~
```

If you see multiple folders called anaconda or miniconda, e.g. anaconda3 and
miniconda2, you have installed multiple versions of conda! Another way to check
is to print your PATH or view your .bashrc / .benv:

```
echo $PATH
cat ~/.bashrc
cat ~/.benv  # if you're on DICE
```

This will show multiple conda directories.

You only need to use one installation of conda, and it doens't matter whether
you use version 2 or 3 (there is no difference that will affect this course).

Simply recreate your environment(s) in one of the conda installations, and
delete the other.

- https://conda.io/docs/user-guide/tasks/manage-environments.html#sharing-an-environment
- https://conda.io/docs/user-guide/install/linux.html#uninstalling-anaconda-or-miniconda
