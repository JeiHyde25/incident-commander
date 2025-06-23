# 🚨 Incident Commander

![MIT License](https://img.shields.io/badge/License-MIT-yellow.svg)  
![Made with Python](https://img.shields.io/badge/Made%20with-Python-blue)

**Incident Commander** is a Python-based CLI tool that automates the creation of ServiceNow incidents. Designed for ITSM workflows, it enables engineers and support teams to log incidents quickly and securely through the command line — or integrate the tool into larger monitoring/alerting systems like Zabbix.

---

## 📁 Project Structure

```
incident-commander/
├── main.py               # CLI entrypoint and incident creator
├── .env.example          # Sample environment variable file
├── incident_log.txt      # Local log file for tracking incidents
├── requirements.txt      # Python dependencies
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

## 🧪 Installation

```bash
git clone https://github.com/JeiHyde25/incident-commander.git
cd incident-commander
pip install -r requirements.txt
cp .env.example .env  # then fill in your credentials
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