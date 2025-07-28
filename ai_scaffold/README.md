# AIBarnes CLI Tool

A command-line interface for interacting with Claude AI using the Anthropic API. This tool allows you to send prompts to Claude and save responses to files.

## Features

- 🤖 **AI Integration**: Chat with Claude AI directly from your terminal
- 📁 **File Output**: Automatically saves AI responses to timestamped files
- ⚙️ **Easy Configuration**: Simple API key setup and management
- 🛠️ **Cross-Platform**: Works on Windows, macOS, and Linux
- 📊 **Status Monitoring**: Check your configuration status anytime

## Installation

### Prerequisites

- Python 3.8 or higher
- pip (Python package installer)

### Step 1: Clone or Download

```bash
# If using git
git clone <your-repo-url>
cd ai_scaffold

# Or download and extract the files to a directory
```

### Step 2: Create Virtual Environment

**Linux/macOS:**
```bash
python3 -m venv venv
source venv/bin/activate
```

**Windows (Command Prompt):**
```cmd
python -m venv venv
venv\Scripts\activate
```

**Windows (PowerShell):**
```powershell
python -m venv venv
venv\Scripts\Activate.ps1
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 4: Get Your Claude API Key

1. Visit [Anthropic Console](https://console.anthropic.com/)
2. Sign up or log in to your account
3. Navigate to API Keys section
4. Create a new API key
5. Copy the key (it starts with `sk-ant-`)

### Step 5: Configure API Key

```bash
python main.py bot configure --api-key sk-ant-your-api-key-here
```

## Setting Up Aliases (Recommended)

To use `aibarnes` command instead of `python main.py`, set up an alias:

### Linux/macOS

**Option 1: Temporary (current session only)**
```bash
alias aibarnes='cd /path/to/your/ai_scaffold && source venv/bin/activate && python main.py'
```

**Option 2: Permanent**

1. Open your shell configuration file:
   ```bash
   # For bash
   nano ~/.bashrc
   
   # For zsh (macOS default)
   nano ~/.zshrc
   
   # For fish
   nano ~/.config/fish/config.fish
   ```

2. Add the alias line:
   ```bash
   # For bash/zsh
   alias aibarnes='cd /path/to/your/ai_scaffold && source venv/bin/activate && python main.py'
   
   # For fish
   alias aibarnes 'cd /path/to/your/ai_scaffold && source venv/bin/activate && python main.py'
   ```

3. Reload your shell configuration:
   ```bash
   # For bash
   source ~/.bashrc
   
   # For zsh
   source ~/.zshrc
   
   # For fish
   source ~/.config/fish/config.fish
   ```

### Windows

**Option 1: Command Prompt (Temporary)**
```cmd
doskey aibarnes=cd /d "C:\path\to\your\ai_scaffold" ^& venv\Scripts\activate ^& python main.py $*
```

**Option 2: PowerShell (Temporary)**
```powershell
function aibarnes { cd "C:\path\to\your\ai_scaffold"; .\venv\Scripts\Activate.ps1; python main.py $args }
```

**Option 3: Permanent PowerShell**

1. Create or edit your PowerShell profile:
   ```powershell
   notepad $PROFILE
   ```

2. Add this function:
   ```powershell
   function aibarnes { 
       cd "C:\path\to\your\ai_scaffold"
       .\venv\Scripts\Activate.ps1
       python main.py $args 
   }
   ```

3. Reload PowerShell or run:
   ```powershell
   . $PROFILE
   ```

**Option 4: Windows Batch File (System-wide)**

1. Create a batch file `aibarnes.bat`:
   ```cmd
   @echo off
   cd /d "C:\path\to\your\ai_scaffold"
   call venv\Scripts\activate
   python main.py %*
   ```

2. Place it in a directory that's in your PATH (like `C:\Windows\System32` or create a custom bin directory)

## Usage

### Check Configuration Status
```bash
aibarnes bot status
```

### Configure API Key
```bash
aibarnes bot configure --api-key sk-ant-your-api-key-here
```

### Send Prompts to AI
```bash
aibarnes bot fetch --prompt "What day of the week was Halloween in 1932?"
```

```bash
aibarnes bot fetch --prompt "Create a bash script that checks system stats and returns results as JSON"
```

### Get Help
```bash
aibarnes --help
aibarnes bot --help
aibarnes bot fetch --help
aibarnes bot configure --help
```

## Examples

### Basic Usage
```bash
# Check if everything is set up
aibarnes bot status

# Ask a simple question
aibarnes bot fetch --prompt "Explain quantum computing in simple terms"

# Generate code
aibarnes bot fetch --prompt "Write a Python function to calculate fibonacci numbers"

# Ask for analysis
aibarnes bot fetch --prompt "What are the pros and cons of remote work?"
```

### Advanced Usage
```bash
# Complex prompts with quotes
aibarnes bot fetch --prompt "Create a REST API using Python Flask with the following endpoints: GET /users, POST /users, GET /users/<id>, PUT /users/<id>, DELETE /users/<id>"

# Multi-line prompts (use quotes)
aibarnes bot fetch --prompt "I need help with:
1. Setting up a Docker container
2. Installing Node.js
3. Creating a simple web server
Please provide step-by-step instructions."
```

## File Output

All AI responses are automatically saved to files in the format:
```
aireturn-YYYY-MM-DD HH:MM:SS.txt
```

These files are created in the same directory where you run the command.

## Configuration File Location

Your API key is stored in:
- **Linux/macOS**: `~/.aibarnes/config.json`
- **Windows**: `C:\Users\<username>\.aibarnes\config.json`

## Troubleshooting

### Common Issues

**1. "No module named 'anthropic'" error**
```bash
# Make sure virtual environment is activated
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows

# Reinstall dependencies
pip install -r requirements.txt
```

**2. "No Claude API key found" error**
```bash
# Configure your API key
aibarnes bot configure --api-key sk-ant-your-api-key-here

# Or check status
aibarnes bot status
```

**3. "Command not found: aibarnes"**
- Make sure you've set up the alias correctly
- Check that the path in your alias is correct
- Restart your terminal after setting up permanent aliases

**4. API Key Issues**
- Verify your API key is correct (starts with `sk-ant-`)
- Check you have credits in your Anthropic account
- Ensure your API key has the necessary permissions

### Getting Support

If you encounter issues:
1. Check the error message carefully
2. Verify your API key is configured: `aibarnes bot status`
3. Make sure all dependencies are installed
4. Check that your virtual environment is activated

## API Costs

This tool uses the Claude API which has usage-based pricing. Check [Anthropic's pricing page](https://www.anthropic.com/pricing) for current rates.

## Security Note

Your API key is stored locally in a configuration file. Never share this file or commit it to version control.

## License

[Add your license here]

## Contributing

[Add contribution guidelines here]
