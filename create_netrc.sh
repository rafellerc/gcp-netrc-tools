#!/bin/bash

set -e

if [ "$#" -ne 1 ]; then
    echo "Usage: bash create_netrc.sh <REGION>"
    exit 1
fi

REGION=$1
MACHINE="${REGION}-python.pkg.dev"

# Get access token
GCP_TOKEN=$(gcloud auth print-access-token)

if [ -z "$GCP_TOKEN" ]; then
    echo "Failed to retrieve GCP access token."
    exit 1
fi

# Write .netrc
cat > "${HOME}/.netrc" <<EOF
machine ${MACHINE}
login oauth2accesstoken
password ${GCP_TOKEN}
EOF

chmod 600 "${HOME}/.netrc"

echo "Successfully wrote .netrc for ${MACHINE} at ${HOME}/.netrc"
