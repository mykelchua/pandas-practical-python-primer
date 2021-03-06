# Vagrant
[Vagrant](http://www.vagrantup.com) is a tool that creates development 
environments from a configuration file call, unsurprisingly, `Vagrantfile`.

We will be using it to create a uniform environment to learn Python in our
class. This allows us to focus on Python rather than the various environment
differences.

Also, most of the time, Python applications are deployed onto Linux servers.  Practicing with a Linux system will better prepare you for your full-time Python employment. ;)

## Prereqs
For our purposes, you must have 
[VirtualBox](https://www.virtualbox.org/wiki/Downloads) installed on your
system to use Vagrant.

## Command Cheatsheet

  * `vagrant up`: 
    * Will create a VM from a `Vagrantfile`.  To make it easy
      for yourself, make sure you are in the directory where the file 
      exists before issuing the command.
    * Also used to restart a VM that you have stopped using 
    `vagrant suspend` or `vagrant halt`.

  * `vagrant ssh`: Will SSH into your VM. This basically means that you
  get a terminal window for your VM.

  * `vagrant suspend`: Stores the entire state of the VM (including memory)
  and stops the VM.

  * `vagrant halt`: Stores the hard-drive state of the VM and stops it.

  * `vagrant destroy`: Obliterates the VM and all contents.
  
## Training Steps

  * In the root folder of this repository is a `Vagrantfile` for everyone to use during class.
  * Use the `vagrant up` and `vagrant ssh` to get to the command line of your VM.
  * It gives us a clean install of an Ubuntu 14.04 VM but does install some requisites that will be needed for our work - namely some development libraries and Git.  If you need to go back in the future and see what it installed (for your own work!) you can see in the [supplemental provision shell script](../misc/vagrant-pyenv-prereqs.sh)