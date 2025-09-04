# super-screen-saver (sss)
screensaver script inspired by [omarchy's](https://omarchy.org/) screensaver

# demo
![demo](sss.gif)

## Table of Contents
- [Demo](#demo)
- [Installation](#installation)
- [Usage](#usage)
- [License](#license)

## Installation 

> [!IMPORTANT]
>
> All commands below should be run in the terminal.

1. Clone the repository & move into it:  
   ```bash
   git clone git@github.com:silentfin/super-screen-saver.git
   cd super-screen-saver
   ```

2. Set up a virtual environment & activate it:
   - Linux/macOS:  
     ```bash
     python3 -m venv .venv
     source .venv/bin/activate
     ```  
   - Windows:  
     ```bash
     python -m venv .venv
     .\.venv\Scripts\activate
     ```  

3. Install dependencies:  
    > [!WARNING]
    >
    >Make sure the virtual environment is activated before you run this command.
   ```bash
   pip install terminaltexteffects
   ```  

## Usage
> [!CAUTION]
>
> Activate your virtual environment before running the script.
- Linux/macOS:  
    ```bash    
    python3 main.py
    ```  
- Windows:  
    ```bash
    python main.py
    ```
*Press `CTRL + C` to stop the script.*
>[!TIP]
>
> Add this alias in your `.bashrc`, `.zshrc` or `.whatever_you_use_rc`
>
> Replace `/add_your_path_here/super-screen-saver` in the alias with the actual full path where you cloned the repository.
>
>```alias sss='(cd /add_your_path_here/super-screen-saver && source .venv/bin/activate && python3 main.py)'```
>
> Reload your terminal after adding the alias.
>
> Now whenever you type `sss` in the terminal, the script will run without manually activating the virtual environment and will deactivate the virtual environment once the script is stopped.

## License
This project is licensed under the [MIT License](LICENSE). See the [LICENSE](LICENSE) file for more details.