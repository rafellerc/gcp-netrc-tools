import subprocess
import sys
from pathlib import Path

def main():
    if len(sys.argv) != 2:
        print("Usage: create-netrc <REGION>")
        sys.exit(1)

    region = sys.argv[1]
    machine = f"{region}-python.pkg.dev"

    try:
        token = subprocess.check_output(
            ["gcloud", "auth", "print-access-token"],
            text=True
        ).strip()
    except subprocess.CalledProcessError:
        print("Failed to retrieve GCP access token.")
        sys.exit(1)

    netrc_content = f"""machine {machine}
login oauth2accesstoken
password {token}
"""

    netrc_path = Path.home() / ".netrc"
    netrc_path.write_text(netrc_content)
    netrc_path.chmod(0o600)

    print(f"Successfully wrote .netrc for {machine} at {netrc_path}")
