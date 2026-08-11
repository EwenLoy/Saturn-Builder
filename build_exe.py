#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Скрипт для сборки EXE файла без консольного окна
"""

import subprocess
import sys
import os

def build_exe():
    """Собирает EXE файл с параметрами для скрытия консольного окна"""
    
    # Проверяем, установлен ли PyInstaller
    try:
        import PyInstaller
        print("✅ PyInstaller найден")
    except ImportError:
        print("❌ PyInstaller не найден. Устанавливаем...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "pyinstaller"])
        print("✅ PyInstaller установлен")
    
    # Параметры для сборки
    cmd = [
        "pyinstaller",
        "--onefile",                    # Один файл
        "--windowed",                   # Без консольного окна (это ключевой параметр!)
        "--name=SaturnBuilder",         # Имя выходного файла
        "--icon=icon.ico",              # Иконка (если есть)
        "--add-data=icon.ico;.",        # Добавляем иконку в ресурсы
        "--hidden-import=PIL._tkinter_finder",  # Важные импорты
        "--hidden-import=customtkinter",
        "--hidden-import=tkinter",
        "--hidden-import=tkinter.ttk",
        "--hidden-import=tkinter.filedialog",
        "--hidden-import=tkinter.messagebox",
        "--hidden-import=tkinter.scrolledtext",
        "--hidden-import=tkinter.simpledialog",
        "--hidden-import=requests",
        "--hidden-import=pyperclip",
        "--hidden-import=psutil",
        "--hidden-import=zipfile",
        "--hidden-import=shutil",
        "--hidden-import=threading",
        "--hidden-import=time",
        "--hidden-import=socket",
        "--hidden-import=datetime",
        "--hidden-import=platform",
        "--hidden-import=base64",
        "--hidden-import=io",
        "--hidden-import=urllib.request",
        "--hidden-import=tarfile",
        "--hidden-import=traceback",
        "--clean",                      # Очистка кэша
        "main.py"                       # Основной файл
    ]
    
    print("🚀 Начинаем сборку EXE файла...")
    print(f"Команда: {' '.join(cmd)}")
    
    try:
        # Запускаем сборку
        result = subprocess.run(cmd, check=True, capture_output=True, text=True)
        print("✅ Сборка завершена успешно!")
        print("📁 EXE файл создан в папке dist/SaturnBuilder.exe")
        
        # Проверяем, что файл создался
        exe_path = "dist/SaturnBuilder.exe"
        if os.path.exists(exe_path):
            size = os.path.getsize(exe_path)
            print(f"📊 Размер файла: {size / (1024*1024):.1f} МБ")
        else:
            print("❌ EXE файл не найден в папке dist/")
            
    except subprocess.CalledProcessError as e:
        print(f"❌ Ошибка сборки: {e}")
        print(f"Вывод: {e.stdout}")
        print(f"Ошибки: {e.stderr}")
        return False
    
    return True

if __name__ == "__main__":
    print("🔧 Saturn Builder - Сборка EXE файла")
    print("=" * 50)
    
    success = build_exe()
    
    if success:
        print("\n🎉 Сборка завершена! Теперь можете запустить SaturnBuilder.exe")
        print("💡 EXE файл будет работать без консольного окна")
    else:
        print("\n❌ Сборка не удалась. Проверьте ошибки выше.")
    
    input("\nНажмите Enter для выхода...")
