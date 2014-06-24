# -*- mode: python -*-
a = Analysis(['cloudsigma_stats.py', 'cloudsigma_stats.spec'],
             pathex=['/home/nikola/src/cloudsme_stats'],
             hiddenimports=[],
             hookspath=None,
             runtime_hooks=None)
pyz = PYZ(a.pure)
exe = EXE(pyz,
          a.scripts,
          a.binaries +  [('requests/cacert.pem', '/home/nikola/.virtualenvs/cloudsme_stats/lib/python2.7/site-packages/requests/cacert.pem', 'DATA'), ],
          a.zipfiles,
          a.datas,
          name='cloudsigma_stats',
          debug=False,
          strip=None,
          upx=True,
          console=True )
