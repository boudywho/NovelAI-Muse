## NovelAI Muse 🎨

NovelAI Muse is a Telegram bot that helps you break through creative block by generating random NovelAI artists and providing essential prompts to kickstart your imagination! 

This bot is perfect for:

* **Finding new NovelAI artists:** Tired of the same old styles? Discover fresh talent with a simple command.
* **Sparking creativity:** Get unique and inspiring prompts tailored for NovelAI image generation. 
* **Exploring new artistic directions:**  Break out of your comfort zone and experiment with different styles and concepts.

### Installation Guide 💻

Follow these steps to install and run NovelAI Muse on your system:

1. **Clone the repository:**

   ```bash
   git clone https://github.com/boudywho/NovelAI-Muse.git
   ```

2. **Navigate to the project directory:**

   ```bash
   cd NovelAI-Muse
   ```

3. **Create a virtual environment:**

   ```bash
   python -m venv venv
   ```

4. **Activate the virtual environment:**

   ```bash
   source venv/bin/activate
   ```

5. **Install the required packages:**

   ```bash
   pip install python-telegram-bot requests
   ```

6. **Obtain your Telegram Bot Token:**

   a. Open Telegram and search for the **BotFather**.

   b. Send the command `/newbot`.

   c. Follow the instructions to name your bot (e.g., "NovelAI Muse Bot").

   d. The BotFather will provide you with a unique **token**. Keep this token safe.

7. **Configure the `bot.py` file:**

   Open the `bot.py` file and locate the `BOT_TOKEN` parameter. 
   Replace `YOUR_TELEGRAM_BOT_TOKEN` with the token you received from BotFather (must be included between quotes"").

   ```python
   BOT_TOKEN = "YOUR_TELEGRAM_BOT_TOKEN" 
   ```

8. **Run the bot:**

   ```bash
   python bot.py 
   ```

   Your bot is now live and ready to receive commands!

### Auto-Start on Arch Linux 🐧

For convenience, you can set up NovelAI Muse to start automatically when your system boots up. Here's how:

1. **Create a systemd service file:**

   ```bash
   sudo nano /etc/systemd/system/novelai-muse.service
   ```

2. **Paste the following content into the file:**

   ```ini
   [Unit]
   Description=NovelAI Muse Telegram Bot
   After=network.target

   [Service]
   User=yourusername
   Group=yourgroup
   WorkingDirectory=/path/to/NovelAI-Muse
   ExecStart=/path/to/venv/bin/python bot.py
   Restart=always
   RestartSec=10

   [Install]
   WantedBy=multi-user.target
   ```

   - Replace `yourusername` and `yourgroup` with your actual username and group.
   - Replace `/path/to/NovelAI-Muse` with the absolute path to your project directory.
   - Replace `/path/to/venv/bin/python` with the absolute path to your virtual environment's Python executable.

3. **Save the file and enable the service:**

   ```bash
   sudo systemctl enable novelai-muse.service
   sudo systemctl start novelai-muse.service
   ```

Now, NovelAI Muse will automatically start whenever your Arch Linux system boots. 

## Using NovelAI Muse:  A Tip ✨

When using the generated prompts from NovelAI Muse, remember to add your own creative ideas **before** the final quality modifiers like "best quality, amazing quality, very aesthetic, absurdres". This ensures your unique vision takes center stage!

---
## Future Development Plans 🚀

NovelAI Muse is constantly evolving! Here are some exciting features we're planning to add:

* **Expanding the artist database:** Continuously updating the bot with new and exciting NovelAI artists. 
* **PNG metadata reader:**  Unlocking hidden information and artistic insights within your NovelAI images.
* **Enhanced prompt generation:** Creating more diverse and specific prompts to fuel your creative journey. 

Stay tuned for updates! ✨ 

## We hope you enjoy using NovelAI Muse to unlock your artistic potential! Happy creating! ✨ 
