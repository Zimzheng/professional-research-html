#!/usr/bin/env sh
# Create an import archive whose root directly contains SKILL.md.
set -eu

script_dir=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
skill_root=$(CDPATH= cd -- "$script_dir/.." && pwd)
output_path=${1:-"$skill_root/dist/professional-research-html.zip"}
output_dir=$(dirname -- "$output_path")

mkdir -p "$output_dir"
git -C "$skill_root" archive --format=zip --output="$output_path" HEAD -- \
  SKILL.md README.md INSTALL.md references agents scripts examples assets

printf 'Created %s\n' "$output_path"
