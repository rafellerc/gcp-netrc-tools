# GCP NetRC Tools

This repository provides a simple tool to dynamically generate `.netrc` files for authenticating to Google Artifact Registry (GAR) using a fresh OAuth2 access token.

It supports:
- A CLI tool (usable via uvx) for convenient execution
- A fallback Bash script for environments where Python or uvx is not available

---

## ✨ Usage

### 1. Using uvx (recommended)

You can run the CLI tool directly without cloning the repository:

Example:

```bash
uvx git+https://github.com/rafael-eller/gcp-netrc-tools.git create-netrc <REGION>
```
For instance:
```bash
uvx git+https://github.com/rafael-eller/gcp-netrc-tools.git create-netrc us-central1
```

This will:
- Obtain a fresh Google Cloud access token
- Create or update `~/.netrc` with the correct credentials
- Restrict file permissions automatically

---

### 2. Using the Bash script (fallback)

If you prefer, or cannot use uvx, you can run the included Bash script manually:

Example:
```bash
bash create_netrc.sh <REGION>
```

For instance:
```bash
bash create_netrc.sh us-central1
```

The behavior is the same as the Python CLI version.

---

## 📚 How It Works

- Authenticates using `gcloud auth print-access-token`
- Writes a `.netrc` entry for the specified region, structured like:

      machine <REGION>-python.pkg.dev
      login oauth2accesstoken
      password <ACCESS_TOKEN>

- Ensures the `.netrc` file is secure by setting permissions to 600

The `.netrc` file allows tools like uv, pip, or twine to authenticate automatically when accessing Google Artifact Registry.

---

## ⚠️ Requirements

- gcloud CLI must be installed and authenticated (gcloud auth login)
- The user must have appropriate permissions to access the target Artifact Registry
- uv (for using uvx) or Bash (for using the script fallback)

---

## 📄 License

This project is licensed under the MIT License.