#!/bin/sh

#if you use conda do this
source /etc/profile
source /opt/anaconda3/bin/activate
conda activate ScriptDev

#if not, just select a right python path
cd /Users/your_account/Desktop/ShellProgramming/FduAutoSubmit
/opt/anaconda3/envs/ScriptDev/bin/python main.py