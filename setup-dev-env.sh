#!/bin/bash

echo "🔧 Setting up development environment..."

# Exit if any command fails
set -e

# Check pip-tools is installed
if ! command -v pip-compile &> /dev/null
then
    echo "❌ pip-compile could not be found. Please run: pip install pip-tools"
    exit 1
fi

# Compile requirements.in
echo "📦 Compiling requirements.in → requirements.txt..."
pip-compile --upgrade requirements.in

# Compile requirements-dev.in
echo "📦 Compiling requirements-dev.in → requirements-dev.txt..."
pip-compile --upgrade requirements-dev.in

# Install dev requirements
echo "📥 Installing development dependencies..."
pip install -r requirements-dev.txt

# Install runtime requirements
echo "📥 Installing development dependencies..."
pip install -r requirements.txt

echo "✅ Development environment setup complete."