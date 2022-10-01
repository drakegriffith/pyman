# 📖 [Getting Started]

> Concepts: `cmd line` `conda` `jupyter`

## 🏕️ Setting up the Environment 

We previously have used IDLE (Integrated Development and Learning Environment) as
our IDE for Python. Instead, we shall switch to **requiring** the installation 
of the package manager [Conda][] to elevate efficiency and convenience for our future.

[Conda]: https://www.anaconda.com/

Before I introduce anything else, ensure the text editor [Visual Studio Code][] is installed
on your system. VS Code is where we will write our code and is accessible to all for free!

[Visual Studio Code]: https://code.visualstudio.com/Download

Conda is an open-source package management system and environment management systen
that runs on Windows, macOS, and Linux. We install packages and add them into our
environment to access modules and methods from within these packages. 
>**Anaconda**, the robust version of Conda, contains over 1500 packages automatically installed at once. 
>**Miniconda** is the condensed version of Conda. Miniconda builds an environment from stratch
> by installing only the packages the individual needs. We'll use `conda install package_name` to install any other packages we need
> through the terminal 📦.

Minidoka can be quicker, but we'll start with Anaconda. Over 250 of the most popular data science 
packages are automatically installed with Anaconda, so it occupies around 3.2 GBs of storage. 

Once Anaconda has installed itself, we'll use our computers command prompt to properly run it. 
Open the Anaconda Navigator through the terminal with `anaconda-navigator` and await the application's 
execution. After Anaconda has opened, launch the Jupityer notebook. We can think of Jupityer notebook as
similar to studying using sticky notes. We seperate important ideas by using multiple stickies.  
Jupityer allows us to create cells and run seperate cells when we want. 

>Jupityer uses the `.ipynb` file extention, originally from iPython. iPython was used for short programs and 
>single-lined commands to enhance efficiency and increase convenience. Jupityer stores our notebook in a 
>JSON format, which is one of the many data exchange formats we use to transport data from language to language.
>JSON can be thought of as a translator between two languages, and will be used later in this course. 

## Terminal Navigation

The file system on our computers is structured like a tree. Just how we can 
navigate through our file system by clicking around our interface on Mac or Windows,
we can also use commands through the terminal to find and access files.

> See the command-line cheatsheet for more helpful hints on the terminal.

Let's find a place to create our new course notebook. Open the terminal and type `ls` to find our original position. 'cd' into another directory using `cd folder_name` and pick a place to put our new notebook. Use `cd -` to go back to your previous location. Finally, type `mkdir new_folder_name` into the terminal, and access this folder using cd 
again. You have created our folder from the command line, impressive!

> We will put our Python programs in this folder for the future. Feeling like a hacker already?

Nice work. Next: Python Re-Review and Data Structures 
