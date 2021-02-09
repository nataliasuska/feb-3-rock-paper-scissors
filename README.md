# Rock, Paper, Scissors Game
### Made with love and coffee by Natalia
Enjoy this fun rock, paper, scissors game to play against the Nat-Bot. Nat-Bot is just a bot version of me, Nat, the creator of this game. 

## Required
+ Anaconda 3.7+
+ Python 3.7+
+ Pip
+ A command-line terminal (I use Git Bash for windows)
+ A text editor for personalization (I use Visual Studio Code)

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
In our new folder, we probably don't have the right packages just yet to customize the player name (more instructuions later) To install it, type in the command line:
```sh
pip install -r requirements.txt
```
Now let's try to run the Python script from the command-line to see if we are set:
```sh
python game.py
```
You should now see that the game begins and prompts you to choose from rock, paper, or scissors. If you already had this game downloaded and want to play again, just be sure to change your directory to the folder where you cloned this repo, activate your environment, and run the game.

### Customizing Player Name
The default name is 'human', since I expect humans to be playing. In order to customize the player name locally in your computer, be sure to have installed the requirements.txt package as mentioned in the Environment Setup and Game Start section above. 

Open your text editor and create a new .env file. In this file, type in your name, or any name within the quotes:
```sh
human_name = "Your Name"
```
Now when we run our app in the command line, we should see "Welcome 'Your Name' to..." rather than "Welcome human to..." Also, we use the variable 'human_name' because I used this for the game code. Thanks to another file, the .gitignore file, your .env file is stored locally and won't be published to GitHub in the event you commit your changes. 




