#!/usr/bin/env python3
import subprocess
import sys
import os

here = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

def run_generator():
    gen = os.path.join(here, 'scripts', 'generate_data.py')
    print('Running data generator:', gen)
    subprocess.run([sys.executable, gen], check=True)

def run_pbir_validator():
    repo_root = os.path.abspath(os.path.join(here, '..'))
    validator = os.path.join(repo_root, '.github', 'skills', 'report-quality-validation', 'scripts', 'validate_pbir_report.py')
    project_name = os.path.basename(here)
    if os.path.exists(validator):
        print('Running PBIR validator...')
        subprocess.run([sys.executable, validator, project_name], check=False)
    else:
        print('PBIR validator not found; skipping')

def main():
    run_generator()
    run_pbir_validator()
    print('✅ ProjectTest1 validation run finished')

if __name__ == '__main__':
    main()
