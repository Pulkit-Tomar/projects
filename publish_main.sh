#!/usr/bin/env bash
set -euo pipefail

cd "$(dirname "$0")"

git add .
commit_message="${1:-Update workspace files}"

git commit -m "$commit_message"
git push origin main
