import os
import datetime
import json
from pathlib import Path

import click
from anthropic import Anthropic


class ConfigManager:
    """
    Handles configuration file management for API tokens and settings
    """
    def __init__(self):
        self.config_dir = Path.home() / ".aibarnes"
        self.config_file = self.config_dir / "config.json"
        self.config_dir.mkdir(exist_ok=True)
    
    def save_config(self, api_key: str):
        """Save the API key to config file"""
        config = {"claude_api_key": api_key}
        with open(self.config_file, 'w') as f:
            json.dump(config, f, indent=2)
        return True
    
    def load_config(self):
        """Load configuration from file"""
        if self.config_file.exists():
            with open(self.config_file, 'r') as f:
                return json.load(f)
        return {}
    
    def get_api_key(self):
        """Get API key from config file or environment variable"""
        config = self.load_config()
        return config.get("claude_api_key") or os.getenv("CLAUDE_API_KEY")


class AIBarnesAgentGenerator:
    """
    class that handles creating client for Anthropic AI model (others can be called as well)
    """
    def __init__(self, ):
        self.config_manager = ConfigManager()
        self.claude_api_key = self.config_manager.get_api_key()
        
        if not self.claude_api_key:
            raise ValueError("No Claude API key found. Please run 'aibarnes bot configure --api-key YOUR_KEY' first.")
        
        self.aiagent = Anthropic(api_key=self.claude_api_key)
        # Get content from Claude

    def ai_agent_brain(self, prompt: str) -> dict:
        client = self.aiagent
        filename = f"aireturn-{datetime.datetime.now()}.txt"
        try:
            response = client.messages.create(
            model="claude-3-haiku-20240307",
            max_tokens=1000,
            messages=[
                {
                    "role": "user",
                    "content": f"{prompt}"
                }
                ])
            content = response.content[0].text  # Extract text from response
            with open(filename, 'w') as f:
                f.write(content)
            response = {
                "timeStamp": f"{datetime.datetime.now()}",
                "fileCreated": True,
                "fileName": f"{filename}",
                "promptAnswer": f"{content}",
                "message": f"File created with the prompt response. filename is {filename}",
                "returnCode": 200
            }
            response = json.dumps(response, indent=4)
            return response
        except Exception as e:
            print(f"Issues running query: {e}")
            return {}

@click.group()
def aibarnes():
    pass

@aibarnes.command()
def info():
    """
    Scaffold for barnesai cli
    """

@aibarnes.group()
def bot():
    pass


@bot.command()
def status():
    """Show current configuration status"""
    config_manager = ConfigManager()
    api_key = config_manager.get_api_key()
    
    if api_key:
        # Mask the API key for security
        masked_key = f"{api_key[:8]}...{api_key[-4:]}" if len(api_key) > 12 else "***"
        click.echo(f"✅ Claude API key configured: {masked_key}")
        click.echo(f"📁 Config file: {config_manager.config_file}")
    else:
        click.echo("❌ No Claude API key configured")
        click.echo("💡 Run 'aibarnes bot configure --api-key YOUR_KEY' to set up your API key.")


@bot.command()
@click.option('--api-key', required=True, help="Your Claude API key from Anthropic")
def configure(api_key: str):
    """Configure Claude API key for aibarnes bot
    
    Example:
    aibarnes bot configure --api-key sk-ant-xxxx-xxxx-xxxx-xxxx
    """
    try:
        config_manager = ConfigManager()
        config_manager.save_config(api_key)
        click.echo("✅ Claude API key configured successfully!")
        click.echo(f"Configuration saved to: {config_manager.config_file}")
    except Exception as e:
        click.echo(f"❌ Error configuring API key: {e}")


@bot.command()
@click.option('--prompt', required=True, help="enter the prompt you want ai to handle")
def fetch(prompt: str):
    """Fetch AI response for a given prompt
    
    Examples:
    aibarnes bot fetch --prompt "create a bash script that checks system stats and return results via json"
    aibarnes bot fetch --prompt "what day of the week was halloween in 1932"
    """
    try:
        ai = AIBarnesAgentGenerator()
        click.echo(ai.ai_agent_brain(prompt))
    except ValueError as e:
        click.echo(f"❌ {e}")
        click.echo("💡 Run 'aibarnes bot configure --api-key YOUR_KEY' to set up your API key.")

if __name__ == "__main__":
    aibarnes()