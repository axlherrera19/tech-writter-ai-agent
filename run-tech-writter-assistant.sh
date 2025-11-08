#!/bin/bash

VENV_PATH="$HOME/dev/personal/tech-writter-ai-agent/venv"

APP_SCRIPT="$HOME/dev/personal/tech-writter-ai-agent/main.py" 

source "$VENV_PATH/bin/activate"

if [ $? -ne 0 ]; then
    echo "ERROR: Could not activate the virtual environment in $VENV_PATH"
    exit 1
fi

"$VENV_PATH/bin/python" "$APP_SCRIPT"

deactivate 

exit $?