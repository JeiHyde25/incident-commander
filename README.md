# 🚨 Incident Commander

![MIT License](https://img.shields.io/badge/License-MIT-yellow.svg)  
![Python](https://img.shields.io/badge/Made%20with-Python-blue)

A Python-based CLI tool that automates the creation of incidents in ServiceNow. This tool simulates real-world ITSM workflows by allowing users to trigger incident reports directly via the terminal. Designed to be extendable and suitable for integration with monitoring tools like Zabbix.

---

## 📁 Project Structure

```
incident-commander/
├── src/
│   └── main.py           # CLI entrypoint
├── .env.example          # Environment variable example file
├── incident_log.txt      # Runtime-generated log file
├── requirements.txt      # Project dependencies
├── setup-dev-env.sh      # Optional setup script
├── .gitignore            # Git ignored files
└── README.md             # Project documentation
```

---

## 🚀 Features

- 🔗 Integration with ServiceNow's REST API
- ✅ Secure credential handling with `.env` files
- 🛠️ Command-line support using `argparse`
- 📋 Logging of all incident activity
- 💡 Easily customizable for real incident fields like urgency/impact

---

## 🖥️ Usage

```bash
python main.py --short "Disk Alert" --desc "Disk usage exceeded 90% on prod-server"
```

> Requires a valid ServiceNow Developer Instance and API access credentials.

---

## 🚀 Tech Stack

- **Python 3.13**
- **Requests**
- **dotenv**
- **argparse**
- **ServiceNow REST API**
- **GitHub**
- **Azure DevOps (Pipelines)**

---

## 🛠️ Getting Started (Local)

### 1. Clone the repository

```bash
git clone https://github.com/JeiHyde25/incident-commander.git
cd incident-commander
```

### 2. Install dependencies  
# Requires Python 3.13+ and pip-tools
```bash
# First, install pip-tools (if not already installed)
pip install pip-tools

# Compile both runtime and dev requirements
pip-compile requirements.in
pip-compile requirements-dev.in

# Install dependencies
pip install -r requirements.txt
pip install -r requirements-dev.txt

# Alternatively, run:
./setup-dev-env.sh

### 3. Set up Git hooks (optional but recommended)
```bash
pre-commit install
```

### 3. Configure environment variables

```bash
cp .env.example .env
# Then edit the `.env` file to include your ServiceNow instance URL, username, and password
```

### 4. Run the CLI tool

```bash
python main.py --short "Server Crash" --desc "App server down, needs urgent reboot."
```

---

## 🎯 Future Enhancements

- [ ] Add urgency and impact levels as CLI flags
- [ ] CSV import for bulk incident creation
- [ ] Streamlit/Flask UI for manual incident input
- [ ] Dockerized CLI runner
- [ ] GitHub Actions CI + Azure Pipelines support

---

## 📜 License

This project is licensed under the MIT License.