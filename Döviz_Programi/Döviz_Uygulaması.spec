# -*- mode: python -*-

block_cipher = None


a = Analysis(['Döviz_Uygulamasý.py'],
             pathex=['C:\\Users\\Greatadamas\\Desktop\\PyQt5 Projesi\\döviz'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='Döviz_Uygulamasý',
          debug=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=False )
