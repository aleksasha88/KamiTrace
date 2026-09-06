#!/usr/bin/env python3
import os
import re
import sys

# 1. Invariant Strings from your Playbook Spec
EXPECTED_LAYERS = [
    "Checklist Layer 1: The Written Layer",
    "Checklist Layer 2: The Audio & Video Layer",
    "Checklist Layer 3: The User Feedback Layer",
    "Checklist Layer 4: The Whistleblower & Disclosures Layer"
]

EXPECTED_SECTIONS = [
    "Section 1: The Origin of the Norms (Input Authority Test)",
    "Section 2: Granularity of Tracking (Processing Resolution Test)",
    "Section 3: Methodological Humility (Fallback Humility Test)"
]

def check_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Rule 1: Check File Structure & Mandatory H1
    filename = os.path.basename(file_path)
    if not re.match(r"^Pillar \d+:", content):
        print(f"❌ Error in {filename}: Missing or malformed H1 Pillar title.")
        return False

    # Rule 2 & 3: Check Invariant Layers and Sections
    for layer in EXPECTED_LAYERS:
        if layer not in content:
            print(f"❌ Error in {filename}: Invariant layer missing -> '{layer}'")
            return False

    for section in EXPECTED_SECTIONS:
        count = len(re.findall(re.escape(section), content))
        if count != 4:
            print(f"❌ Error in {filename}: '{section}' must appear exactly 4 times (found {count}).")
            return False

    # Rule 4: Check the 4-Metric Budget per Layer
    # Splits file by layer and counts the checklist items [ ] inside each block
    layer_blocks = re.split(r"### Checklist Layer \d:", content)[1:]
    if len(layer_blocks) != 4:
        print(f"❌ Error in {filename}: Expected exactly 4 layer blocks.")
        return False

    for idx, block in enumerate(layer_blocks, 1):
        metric_count = len(re.findall(r"\*\s+\[ \]\s+\*\*\[Verification Test", block))
        if metric_count != 4:
            print(f"❌ Error in {filename}: Layer {idx} has {metric_count} metrics. The playbook requires exactly 4.")
            return False

    return True

def main():
    # Targets your formatted pillar files
    target_files = [f for f in os.listdir('.') if f.endswith('.md') and f != 'README.md' and not f.startswith('ARCHITECTURE') and not f.startswith('CONTRIBUTING')]
    
    if not target_files:
        print("⚠️ No pillar markdown files found to lint.")
        sys.exit(0)

    success = True
    for file in target_files:
        if not check_file(file):
            success = False

    if not success:
        print("\n🚨 KamiTrace Architecture Linter Failed. Fix errors before committing.")
        sys.exit(1)
        
    print("\n✅ All pillars match the 96-test symmetric architecture matrix perfectly.")
    sys.exit(0)

if __name__ == "__main__":
    main()
