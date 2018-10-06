# -*- mode: python -*-

block_cipher = None


a = Analysis(['PythonApplication_LearnPyqt5_02.py'],
             pathex=['C:\\Users\\crige\\source\\repos\\Learn_Pyqt5\\PythonApplication_LearnPyqt5_01\\PythonApplication_LearnPyqt5_01'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          [],
          exclude_binaries=True,
          name='PythonApplication_LearnPyqt5_02',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=True )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               name='PythonApplication_LearnPyqt5_02')
