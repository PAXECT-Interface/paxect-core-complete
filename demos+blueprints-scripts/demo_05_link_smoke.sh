#!/usr/bin/env bash
set -u

# Find script location and project root
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ROOT_DIR="${SCRIPT_DIR}"

TMP_BASE="/tmp/paxect_demo_05"
BASEFILE="${TMP_BASE}/paxect_link_hashes.baseline"
mkdir -p "${TMP_BASE}"

FILES=(
  "paxect_link_plugin.py"
  "paxect_core_plugin.py"
  "paxect_aead_hybrid_plugin.py"
  "paxect_polyglot_plugin.py"
  "paxect_selftune_plugin.py"
)

echo "=== PAXECT Demo 05 — Link Smoke Test ==="
echo "Project root: ${ROOT_DIR}"
echo

missing=0
for f in "${FILES[@]}"; do
  if [ ! -f "${ROOT_DIR}/${f}" ]; then
    echo "MISSING: ${f}"
    missing=$((missing+1))
  else
    echo "FOUND: ${f}"
  fi
done

if [ "${missing}" -gt 0 ]; then
  echo
  echo "ERROR: ${missing} files missing in ${ROOT_DIR}"
  exit 1
fi

echo
if command -v dos2unix >/dev/null 2>&1; then
  echo "Normalizing line endings..."
  for f in "${FILES[@]}"; do
    dos2unix -q "${ROOT_DIR}/${f}" 2>/dev/null || true
  done
fi

echo
echo "Setting executable permissions..."
for f in "${FILES[@]}"; do
  chmod +x "${ROOT_DIR}/${f}" 2>/dev/null || true
done

echo
HASHFILE="${TMP_BASE}/current_hashes.txt"
echo "Computing SHA256..."
> "${HASHFILE}"

for f in "${FILES[@]}"; do
  (cd "${ROOT_DIR}" && sha256sum "${f}" 2>/dev/null || shasum -a 256 "${f}" 2>/dev/null) >> "${HASHFILE}"
done

if [ ! -f "${BASEFILE}" ]; then
  cp "${HASHFILE}" "${BASEFILE}"
  echo "✓ Baseline created"
  echo "✓ NO DRIFT"
  exit 0
fi

if diff -u "${BASEFILE}" "${HASHFILE}" >/dev/null 2>&1; then
  echo "✓ NO DRIFT — hashes match"
  exit 0
else
  echo "✗ DRIFT DETECTED"
  diff -u "${BASEFILE}" "${HASHFILE}" || true
  exit 2
fi

