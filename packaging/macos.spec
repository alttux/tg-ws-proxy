# -*- mode: python ; coding: utf-8 -*-

import sys
import os

block_cipher = None

# customtkinter ships JSON themes + assets that must be bundled
import customtkinter
ctk_path = os.path.dirname(customtkinter.__file__)

a = Analysis(
    [os.path.join(os.path.dirname(SPEC), os.pardir, 'macos.py')],
    pathex=[],
    binaries=[],
    datas=[(ctk_path, 'customtkinter/')],
    hiddenimports=[
        'pystray._darwin',
        'PIL._tkinter_finder',
        'customtkinter',
        'cryptography.hazmat.primitives.ciphers',
        'cryptography.hazmat.primitives.ciphers.algorithms',
        'cryptography.hazmat.primitives.ciphers.modes',
        'cryptography.hazmat.backends.openssl',
    ],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    cipher=block_cipher,
    noarchive=False,
)

icon_path = os.path.join(os.path.dirname(SPEC), os.pardir, 'icon.icns')
if not os.path.exists(icon_path):
    icon_path = None

if icon_path:
    a.datas += [('icon.icns', icon_path, 'DATA')]

# Also include .ico fallback
ico_path = os.path.join(os.path.dirname(SPEC), os.pardir, 'icon.ico')
if os.path.exists(ico_path):
    a.datas += [('icon.ico', ico_path, 'DATA')]

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='TgWsProxy',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=True,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)

coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='TgWsProxy',
)

app = BUNDLE(
    coll,
    name='TgWsProxy.app',
    icon=icon_path,
    bundle_identifier='com.tgwsproxy.app',
    info_plist={
        'NSHighResolutionCapable': True,
        'LSUIElement': True,          # hide from Dock, show only in menu bar
        'CFBundleShortVersionString': '1.0.0',
        'CFBundleName': 'TG WS Proxy',
        'NSRequiresAquaSystemAppearance': False,
    },
)
