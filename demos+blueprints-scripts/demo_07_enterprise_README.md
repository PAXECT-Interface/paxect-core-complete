# PAXECT Demo 07 Enterprise – 24/7 Stability Test

Production-grade self-tuning system for long-running deployments.

## Quick Start (Manual Test)

Run for 60 seconds with safe mode:
```bash
chmod +x demo_07_enterprise_stability.py
SAFE_MODE=1 RUN_SECONDS=60 ITERATION_S=5 python3 demo_07_enterprise_stability.py
```

## 24-Hour Production Run

Default 24-hour stability test:
```bash
chmod +x demo_07_enterprise_stability.py
python3 demo_07_enterprise_stability.py
```

Monitor logs in real-time:
```bash
tail -f /tmp/paxect_enterprise_stability.jsonl
```

## Systemd Service (Auto-restart on Boot)

### 1. Create Service File
```bash
sudo nano /etc/systemd/system/paxect-enterprise-stability.service
```

Paste this configuration:
```ini
[Unit]
Description=PAXECT Enterprise Stability Demo
After=network.target

[Service]
Type=simple
User=YOUR_USER_HERE
WorkingDirectory=/home/YOUR_USER_HERE
ExecStart=/usr/bin/python3 /home/YOUR_USER_HERE/demo_07_enterprise_stability.py
Restart=on-failure
RestartSec=5
Environment=SAFE_MODE=0

StandardOutput=append:/var/log/paxect_enterprise_stability.log
StandardError=append:/var/log/paxect_enterprise_stability.log

[Install]
WantedBy=multi-user.target
```

**Replace `YOUR_USER_HERE` with your actual username!**

### 2. Enable and Start Service
```bash
sudo systemctl daemon-reload
sudo systemctl enable paxect-enterprise-stability.service
sudo systemctl start paxect-enterprise-stability.service
```

### 3. Monitor Service

Check status:
```bash
sudo systemctl status paxect-enterprise-stability
```

Watch logs live:
```bash
sudo journalctl -u paxect-enterprise-stability -f
```

Stop service:
```bash
sudo systemctl stop paxect-enterprise-stability
```

## Environment Variables

| Variable | Default | Description |
|----------|---------|-------------|
| `SAFE_MODE` | 0 | Enable validation (1=on, 0=off) |
| `RUN_SECONDS` | 86400 | Runtime (24 hours default) |
| `ITERATION_S` | 5 | Seconds between cycles |

## Log Files

- **JSONL log:** `/tmp/paxect_enterprise_stability.jsonl`
- **Systemd log:** `/var/log/paxect_enterprise_stability.log`

## Analysis

View last 10 cycles:
```bash
tail -n 10 /tmp/paxect_enterprise_stability.jsonl | jq
```

Count total cycles:
```bash
wc -l /tmp/paxect_enterprise_stability.jsonl
```
