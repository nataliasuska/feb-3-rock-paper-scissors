# Rock, Paper, Scissors Game
### Made with love and coffee by Natalia

## Required
+ Anaconda 3.7+
+ Python 3.7+
+ Pip
+ A command-line terminal (I use Git Bash for windows)

## User Instructions
### Cloning
Clone this repository by your own preferences (ZIP folder, command-line, or using GitHub Desktop software). Upon completion, choose a familiar download location. I use my Desktop. If you would like to make any changes to the game, then fork it before cloning. 

### Environment Setup and Game Start
After cloning this repo, navigate to it from your command line terminal. Since I just put it in my desktop, it will look like this for me, but may look different for you:
```sh
cd ~/Desktop/feb-3-rock-paper-scissors
```
Create and activate a new project-specific Anaconda virtual environment for our game titled my-game-env (but you can use a different title), and activate it:
```sh
conda create -n my-game-env python=3.8
conda activate my-game-env
```
In our new folder, we probably don't have the right packages just yet. However, in the requirements.txt file of this repo, I included the package we need for this game. To install it, type in the command line:
```sh
pip install -r requirements.txt
```
Now let's try to run the Python script from the command-line to see if we are set:
```sh
python game.py
```
You should now see that the game begins and prompts you to choose from rock, paper, or scissors. If you already had this game downloaded and want to play again, just be sure to change your directory to the folder where you cloned this repo, activate your environment, and run the game.

### Customizing Player Name



Finally, update your program to allow the user to configure their own player name by passing an environment variable called "PLAYER_NAME" stored in a local ".env" file.

Make sure to add corresponding instructions to the README file, to let the player know how to set up the ".env" file.

Make sure the repository's ".gitignore" file includes an entry about the ".env" file, and ensure the ".gigitnore" file is saved and committed before adding a ".env" file. This should already be the case if you added a Python-flavored ".gitignore" file during the repo creation step.

Also note we are now requiring the program to use a third-party package, so we should add a "requirements.txt" file to the repo with the package name inside. And we should add a `pip install -r requirements.txt` step to the README file to instruct the user to install packages before trying to run the program.
