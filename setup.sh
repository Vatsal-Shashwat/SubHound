#!/bin/bash

# Color codes
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Check if setup has been run before
if [ -n "$SUBHOUND_SETUP_COMPLETED" ]; then
    echo -e "${YELLOW}Subhound setup has already been completed. You can now use the tool from anywhere in your terminal.${NC}"
    exit 0
fi

# Display message for first-time setup
echo -e "${GREEN}Welcome to Subhound setup!${NC}"
echo -e "${GREEN}This script will install and configure Subhound.${NC}"
echo -e "${GREEN}Please follow the instructions to complete the setup.${NC}"
echo ""

# setup commands 
python3 -m pip install -r requirements.txt
pip install --upgrade requests-toolbelt

# Copy or install subhound.py to its appropriate location

# Create a symbolic link to subhound.py in /usr/local/bin
if [ -f /usr/local/bin/subhound ]; then
    echo -e "${YELLOW}Symbolic link already exists. Skipping creation.${NC}"
else
    ln -s /$PWD/subhound.py /usr/local/bin/subhound
    if [ $? -eq 0 ]; then
        echo -e "${GREEN}Symbolic link created successfully.${NC}"
    else
        echo -e "${RED}Failed to create symbolic link.${NC}"
        echo -e "${RED}You may need to run this script with sudo.${NC}"
        exit 1
    fi
fi

# Set executable permissions for subhound.py
chmod +x /$PWD/subhound.py

# Check if the symbolic link creation was successful
if [ $? -eq 0 ]; then
    echo -e "${GREEN}Subhound setup completed successfully! You can now use the tool from anywhere in your terminal.${NC}"
else
    echo -e "${RED}Failed to set executable permissions for subhound.py.${NC}"
    exit 1
fi

# Set environment variable to indicate setup completion
export SUBHOUND_SETUP_COMPLETED=true

