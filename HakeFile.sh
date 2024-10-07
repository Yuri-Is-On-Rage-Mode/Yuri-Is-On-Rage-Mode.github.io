#!/bin/bash

# Variables
APP_NAME="hmzas-website"
REPO_URL="https://github.com/Yuri-Is-On-Rage-Mode/Yuri-Is-On-Rage-Mode.github.io.git"

# Step 1: Create a new Svelte app
echo "Creating a new Svelte app named $APP_NAME..."
npx degit sveltejs/template $APP_NAME

# Step 2: Navigate to the app directory
cd $APP_NAME || { echo "Failed to enter the directory"; exit 1; }

# Step 3: Install dependencies
echo "Installing dependencies..."
npm install

# Step 4: Build the app
echo "Building the app..."
npm run build

# Step 5: Initialize a Git repository if it doesn't exist
if [ ! -d .git ]; then
    echo "Initializing Git repository..."
    git init
fi

# Step 6: Add remote repository
git remote add origin $REPO_URL 2>/dev/null || echo "Remote origin already set."

# Step 7: Add files to the repository
echo "Adding files to Git..."
git add .

# Step 8: Commit the changes
git commit -m "Initial commit of $APP_NAME"

# Step 9: Push to GitHub
echo "Pushing to GitHub..."
git push -u origin main  # Change 'main' to 'master' if your default branch is 'master'

echo "Svelte app '$APP_NAME' created and pushed to $REPO_URL"
