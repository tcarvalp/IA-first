"""
Script para gerar o .exe do formulário de Assessment.
Uso: python build_exe.py
"""

import subprocess
import sys
import os

def main():
    # Diretório do projeto
    project_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Comando PyInstaller
    cmd = [
        sys.executable, "-m", "PyInstaller",
        "--onefile",
        "--name", "AssessmentSquadExtrato",
        "--add-data", f"templates{os.pathsep}templates",
        "--add-data", f"config.py{os.pathsep}.",
        "--add-data", f"perguntas.py{os.pathsep}.",
        "--hidden-import", "config",
        "--hidden-import", "perguntas",
        "--icon", "NONE",
        "--console",
        "app.py"
    ]

    print("=" * 60)
    print("  Gerando .exe do Assessment Squad Extrato...")
    print("=" * 60)
    print(f"\nComando: {' '.join(cmd)}\n")

    result = subprocess.run(cmd, cwd=project_dir)

    if result.returncode == 0:
        exe_path = os.path.join(project_dir, "dist", "AssessmentSquadExtrato.exe")
        print("\n" + "=" * 60)
        print(f"  ✅ .exe gerado com sucesso!")
        print(f"  📁 Local: {exe_path}")
        print("=" * 60)
    else:
        print("\n❌ Erro ao gerar .exe")
        sys.exit(1)


if __name__ == "__main__":
    main()
