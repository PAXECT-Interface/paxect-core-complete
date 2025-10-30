import subprocess

def show_message(title, text):
    subprocess.run(["zenity", "--info", "--title", title, "--text", text])

def run_plugin(plugin_file):
    show_message("Installing Plugin", f"Installing {plugin_file}...")
    subprocess.run(["python3", plugin_file, "install"])

def install_grafana():
    result = subprocess.run(["which", "grafana-server"], capture_output=True)
    if result.returncode != 0:
        show_message("Grafana", "Grafana is not installed. Installing now...")
        subprocess.run(["sudo", "apt-get", "update"])
        subprocess.run(["sudo", "apt-get", "install", "-y", "grafana"])

def configure_dashboard():
    show_message("Grafana", "Importing PAXECT dashboard and datasource...")

    subprocess.run([
        "curl", "-X", "POST", "http://localhost:3000/api/datasources",
        "-H", "Content-Type: application/json",
        "-H", "Authorization: Bearer <API_KEY>",
        "-d", "@grafana/paxect-datasource.json"
    ])

    subprocess.run([
        "curl", "-X", "POST", "http://localhost:3000/api/dashboards/db",
        "-H", "Content-Type: application/json",
        "-H", "Authorization: Bearer <API_KEY>",
        "-d", "@grafana/paxect-dashboard.json"
    ])

def launch_dashboard():
    subprocess.run(["systemctl", "start", "grafana-server"])
    subprocess.run(["xdg-open", "http://localhost:3000/d/paxect"])

def main():
    show_message("PAXECT Installer", "Starting installation of PAXECT Core Complete...")

    plugins = [
        "paxect_core_plugin.py",
        "paxect_aead_hybrid_plugin.py",
        "paxect_selftune_plugin.py",
        "paxect_link_plugin.py",
        "paxect_polyglot_plugin.py"
    ]

    for plugin in plugins:
        run_plugin(plugin)

    install_grafana()
    configure_dashboard()
    launch_dashboard()

    show_message("Installation Complete", "✅ PAXECT Core Complete has been successfully installed.")

if __name__ == "__main__":
    main()

