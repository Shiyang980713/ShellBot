# Auto Submit Bot
Auto submit bot for fudan covid-19

This is a simple python bot for daily check in ping'an fudan covid-19

There is a .sh example, but you should make a **.sh file** according to **your own device.**

**Make sure** that some important **env packages** are installed:

- **selenium**
- **webdriver_manager**
- *pytesseract & PIL are not necessary, they are used for checking your id again (After the bot log in the web), if you don't need that, just comment out the corresponding code(line50-59 and import line)*

**Crontab** is recommended for timed automation task.

You **might** need to **shutdown** your **VPN** proxy for a **right ip location**. 

**Enjoy!**

